import os
import simpleaudio
import argparse
import nltk
import numpy as np

from nltk.corpus import cmudict
import re

### NOTE: DO NOT CHANGE ANY OF THE EXISTING ARGUMENTS
nptype=np.int16

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
            wav_folder = wav_folder if wav_folder is not None else []
            allfile = []
            for root, dirnames, filenames in os.walk(wav_folder):
                # for dir in dirnames:
                # allfile.append(os.path.join(root,dir))
                for word in wav_folder:
                    for name in word:
                        name = name + '.wav'
                        allfile.append(os.path.join(root, name))
                        # print (os.path.join(root, name))
            return allfile



class playing():
    def __init__(self,args,out,S):
        self.args=args
        self.out=simpleaudio.Audio(rate=1600)
        self.S=S



    def process(self):
        #Folder containing monophone wavs
        if self.args.monophones is not None:
            phoneme = self.get_phone(args.phrase[0])
            #print(phoneme)
            wavfile = self.S.get_wavs(phoneme)
           # print(wavfile)
            voice_data = self.wava_data(phoneme,wavfile)
            #print(voice_data)

            self.out.data = voice_data
            if self.args.outfile is not None:
               self.out.save(self.args.outfile)

             #Play the output audio
            if self.args.play:
               self.out.play()

              #Change the volume
            if self.args.volume is not None:
               self.out.rescale(self.args.volume)



    # normalize the input text
    def get_words(self,phrase):
        print(phrase)
        tokens=[]
        punctuation=[]
        word_pattern = r'(\w+)'
        comma_pattern=r'(,)'
        period_pattern=r'(.)'
        question_pattern=r'(?)'

        #phrase = input('please input your text:')
        tokens = nltk.tokenize.regexp_tokenize(phrase, word_pattern)
        tokens_lower=[item.lower() for item in tokens]

        return (tokens_lower)
        #tokens= nltk.regexp_tokenize(text,pattern)

    # get every word's phonemeset from cmudict
    # it returns a list contains phoneme(without any digital numbers)
    def get_phone_seq(self,phrase):
        phoneme=[]
        entries = cmudict.dict()
        print(len(entries))
        for tokens_lower in phrase.get_words():
            try:
                words=entries[tokens_lower]
                words = [item.lower() for item in words]
                words = nltk.tokenize.regexp_tokenize(str(words), r'([a-z]{1,2})')
            except KeyError:
                input('Please change your input:')
        phoneme.append(words)
        return (phoneme)
        # example return[['hh','ah','l','ow'],['w','er','l','d']]

    def wav_data(self, phoneme, wavfile,):
        voice_data = np.array([], dtype=nptype)
        for elements in wavfile:
            for elements1 in phoneme:
                out.load(elements1)
                voice_data = np.append(voice_data, out.data)
        return voice_data



if __name__ == "__main__":
    S = Synth(wav_folder=args.monophones)

  # phone_seq = get_phone_seq(args.phrase[0])
  # filePath = '/Users/apple/Downloads/cpslp-assignment-4/monophones'

    #allfile = get_wavs(self)
    #print(file)

    # out is the Audio object which will become your output
    # you need to modify out.data to produce the correct synthesis
    out = simpleaudio.Audio(rate=16000)
    print(out.data, type(out.data))


