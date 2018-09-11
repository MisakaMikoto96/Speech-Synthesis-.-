import argparse
import os
import re
import numpy as np
from nltk.corpus import cmudict

import simpleaudio

nptype = np.int16

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
# print(args)

# print(args.monophones)


class Synth(object):
    def __init__(self, wav_folder):
        self.phones = {}
        self.get_wavs(wav_folder)

    def get_wavs(self, wav_folder):
        for root, dirs, files in os.walk(wav_folder, onerror=self.folder_erroe, topdown=False):
            for file in files:
                phone = re.match(r"(?P<phone>\w*)", file).group("phone")
                self.phones[phone.upper()] = wav_folder + "/" + file
        try:
            if len(self.phones) != 40:
                raise FolderError
        except FolderError:
            print("FolderError: Choose a wrong folder")
            exit()



    @staticmethod
    def folder_erroe(FolderError):
        print("FolderError: " + FolderError.args[1])
        exit()

    def get_wavs_seq(self, phone_sequence):
        patten = re.compile(r"(?P<wave>[a-zA-z]*)")
        return [[self.phones[re.match(patten, x).group("wave").upper()]
                for x in y if re.match(patten, x).group("wave").upper() in self.phones.keys()]
                for y in phone_sequence]

    def get_stress_pos(self, phone_sequence):
        stress_pos = {}
        patten = re.compile(r"(?P<stress>\d?)$")
        for word in phone_sequence:
            for phone in word:
                result = re.search(patten, phone)
                stress_pos[phone] = result.group("stress")
        return stress_pos
        # patten = re.compile(r"(?P<stress>\d?)$")
        # return [[re.search(patten, x).group("stress") for x in y] for y in phone_sequence]



class FolderError(Exception):
    pass



class process():

    def __init__(self, args, out, S):
        self.args = args
        self.out = out
        self.S = S

    def generate(self):
        if self.args.monophones is not None:
            phone_seq = self.get_phone_seq(args.phrase[0])
            print(phone_seq)
            waves_seq = self.S.get_wavs_seq(phone_seq)
            print(waves_seq)
            stress_seq = self.S.get_stress_pos(phone_seq)
            print(stress_seq)
            voice_data = self.get_voice_data(phone_seq, waves_seq, stress_seq)
            print(voice_data)
            self.push_data(voice_data)
            if self.args.volume:
                self.change_volume()
            if self.args.play:
                self.synth_play()
            if self.args.outfile:
                self.store_wav()

    def get_phone_seq(self, phrase):
        result1 = re.sub(r'[^a-zA-Z0-9 ,.?]', '', phrase)  # remove all characters we don't want
        result2 = re.sub(r'[,]', ' ,', result1)
        result3 = re.sub(r'[.]', ' .', result2)
        result4 = re.sub(r'[?]', ' ?', result3)
        result5 = re.sub(r'[1-9]', '', result4)  # replace all number with ""
        resultx = result5.lower()  # turn all English alphabet into low case
        transcr = cmudict.dict()
        phone_sequence = []
        for word in resultx.split(" "):
            if word == "," or word == "." or word == "?":
                phone_sequence.append(word)
            else:
                try:
                    phone_sequence.append(transcr[word][0])
                except Exception as e:
                    print("The {} is not in the cmudict.".format(e))
                    exit()
        return phone_sequence

    def get_voice_data(self, phone_seq, waves_seq, stress_seq):
        voice_data = np.array([], dtype=nptype)
        for (wordf, word) in zip(waves_seq, phone_seq):
            for (phonef, phone) in zip(wordf, word):
                out.load(phonef)
                # print(out.data, type(out.data))
                if stress_seq[phone] is None:
                    pass
                elif stress_seq[phone] == "1":
                    self.out.rescale(0.6)
                elif stress_seq[phone] == "2":
                    self.out.rescale(0.7)
                elif stress_seq[phone] == "0":
                    self.out.rescale(0.4)
                voice_data = np.append(voice_data, out.data)
        return voice_data

    def change_volume(self):
        self.out.rescale(self.args.volume)

    def push_data(self, voice_data):
        self.out.data = voice_data

    def synth_play(self):
        self.out.play()

    def store_wav(self):
        self.out.save(self.args.outfile)



if __name__ == "__main__":
    S = Synth(wav_folder=args.monophones)
    # out is the Audio object which will become your output
    # you need to modify out.data to produce the correct synthesis
    out = simpleaudio.Audio(rate=16000)

    P = process(args, out, S)
    P.generate()










