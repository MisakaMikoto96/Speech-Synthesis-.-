import os
import simpleaudio
import argparse
import numpy as np
import string
from nltk.corpus import cmudict
import re

number_str = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
              9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
              16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}

order_str = {1: 'first', 2: 'second', 3: 'third', 4: 'fourth', 5: 'fifth', 6: 'sixth', 7: 'seventh', 8: 'eighth',
             9: 'ninth', 10: 'tenth', 11: 'eleventh', 12: 'twelfth', 13: 'thirteenth', 14: 'fourteenth',
             15: 'fifteenth',
             16: 'sixteenth', 17: 'seventeenth', 18: 'eighteenth', 19: 'nineteenth', 20: 'twentieth',
             21: 'twenty first',
             22: 'twenty second', 23: 'twenty third', 24: 'twenty fourth', 25: 'twenty fifth', 26: 'twenty sixth',
             27: 'twenty seventh', 28: 'twenty eighth', 29: 'twenty ninth', 30: 'thirtieth', 31: 'thirty first'}

month_str = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
             9: 'September', 10: 'October', 11: 'November', 12: 'December'}

d_str = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty'
    , 9: 'ninety'}

### NOTE: DO NOT CHANGE ANY OF THE EXISTING ARGUMENTS
parser = argparse.ArgumentParser(
    description='A basic text-to-speech app that synthesises an input phrase using monophone unit selection.')
parser.add_argument('--monophones', default="./monophones", help="Folder containing monophone wavs")
parser.add_argument('--play', '-p', action="store_true", default=False, help="Play the output audio")
parser.add_argument('--outfile', '-o', action="store", dest="outfile", type=str, help="Save the output audio to a file",
                    default=None)
parser.add_argument('phrase', nargs=1, help="The phrase to be synthesised")

# Arguments for extensions
parser.add_argument('--spell', '-s', action="store_true", default=False,
                    help="Spell the phrase instead of pronouncing it")
parser.add_argument('--volume', '-v', default=None, type=float,
                    help="A float between 0.0 and 1.0 representing the desired volume")

args = parser.parse_args()

print(args.monophones)

class Synth(object):
    def __init__(self, wav_folder):
        self.phones = {}
        self.get_wavs(wav_folder)

    def get_wavs(self, wav_folder):
        for root, dirs, files in os.walk(wav_folder, topdown=False):
            for file in files:
                x = simpleaudio.Audio(rate=1600)
                x.load(os.path.join(root,file))
                self.phones[os.path.splitext(file)[0]] = x
        #punctuation silence
        comma_250ms = simpleaudio.Audio()
        comma_250ms.add_echo(1,250)
        punctuation_500ms = simpleaudio.Audio()
        punctuation_500ms.add_echo(1,500)
        self.phones[','] = comma_250ms
        self.phones['.'] = punctuation_500ms
        self.phones['?'] = punctuation_500ms
        self.phones['!'] = punctuation_500ms


def replace(old, new, line):
    for s in old:
        line = line.replace(s, new)
    return line

"""
    replace the numbers in the phrase to the corresponding english text
"""
def replace_number(phrase):
    words = re.split('\\s+', phrase)
    for word in words:
        if word.replace('.', '', 1).isdigit():
            if '.' in word:
                phrase = phrase.replace(word, float_number(word))
            else:
                phrase = phrase.replace(word, translate_number(word))
        return phrase

"""
    replace the date in the phrase to the corresponding english text
"""
def replace_date(phrase):
    words = re.split("\\s+", phrase)
    for word in words:
        if re.match(r'(\d{1,2}/\d{2})', word) is not None or re.match(r'(\d{1,2}/\d{2}/\d{2})', word) is not None or re.match(r'(\d{1,2}/\d{2}/\d(4))', word) is not None:
            tokens = word.split('/')
            date_str = ''
            if len(tokens) == 2:
                day = int(tokens[0])
                month = int(tokens[1])
                date_str += 'the '+order_str[day]
                date_str += ' of '
                date_str += month_str[month]
            else:
                day = int(tokens[0])
                month = int(tokens[1])
                year = int(tokens[2])
                if year < 1000:
                    year += 1900
                date_str += 'the ' + order_str[day]
                date_str += ' of '
                date_str += month_str[month]
                date_str += ' ' + translate_number(year //100) + ' ' + translate_number(year % 100)
            phrase = phrase.replace(word, date_str)
    return phrase


def get_phone_seq(phrase):
    phrase = replace_number(phrase)
    phrase = re.sub(r'[,]', ' ,', phrase)
    phrase = re.sub(r'[!]', ' !', phrase)
    phrase = re.sub(r'[.]', ' .', phrase)
    phrase = re.sub(r'[?]', ' ?', phrase)
    phrase = replace_date(phrase)
    punctuation = """!"#$%&'()*+-./:;<=>@[\]^_`|~"""
    replace_phrase = replace(punctuation, "", phrase)
    replace_phrase = replace_phrase.lower()
    words = re.split('\\s+',replace_phrase)

    phone_seq = []
    stress_seq = []

    for word in words:
        if word == '':
            continue
        if word == ',' or word == '.' or word == '?' or word == '!':
            phone_seq.append(word)
            stress_seq.append(False)
        else:
            emphasize = word
            if '{' in word:
                emphasize = replace('{}', '', word)
            seqs = cmudict.dict()[emphasize]
            for phoneme in seqs[0]:
                if '{' in word:
                    stress_seq.append(True)
                else:
                    stress_seq.append(False)
                m_phone = phoneme.lower()
                m_phone = replace(string.digits, '', m_phone)
                phone_seq.append(m_phone)
    return phone_seq, stress_seq

"""
    translate the integer number to the corresponding english text
"""
def translate_number(number):
    number = int(number)
    if number == 0:
        return 'zero'
    str = ''
    a = number // 100
    number = number % 100
    if a > 0:
        str += number_str[a] + ' hundred'
        if number > 0:
            str += ' and'
    if number > 0:
        if number < 20:
            str += ' ' + number_str[number]
        else:
            a = number // 10
            str += ' ' + d_str[a]
            a = number % 10
            if a > 0:
                str += ' ' + number_str[a]
    return str

"""
    translate the float number to the corresponding english text
"""
def float_number(digital_number):
    number = digital_number[:digital_number.index('.')]
    str = translate_number(number)
    str += 'point'
    for s in digital_number[:digital_number.index(',') + 1:]:
        str += ' ' + number_str[int(s)]
    return str


if __name__ == "__main__":
    S = Synth(wav_folder=args.monophones)

    phone_seq, stress_seq = get_phone_seq(args.phrase[0])

    audio_list=[]

    index=0
    for phone in phone_seq:
        if stress_seq[index]:
            S.phones[phone].rescale(0.8)
        audio_list.append(S.phones[phone])
        index +=1

    # out is the Audio object which will become your output
    # you need to modify out.data to produce the correct synthesis

    #creat the out audio
    out = simpleaudio.Audio(rate=16000)
    voice_data=np.array([], dtype=np.int16)
    for audio in audio_list:
        voice_data=np.append(voice_data, audio.data)
    out.data=voice_data

    # Save the files
    if args.outfile:
       out.save(args.outfile)

    # Play the output audio
    if args.play:
       out.play()

    # Change the volume
    if args.volume:
       out.rescale(args.volume)