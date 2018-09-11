'''import re
import nltk


r=r'(\w+)'
text='ASDF,SADFD,as，sdfewt'
tokens=nltk.regexp_tokenize(text,r)
tokens1=tokens.upper()

print(tokens1)'''

import re

import os
import simpleaudio
import argparse
import nltk
from nltk.corpus import cmudict
import re
import numpy as np

nptype=np.int16

filePath='/Users/apple/Downloads/cpslp-assignment-4/monophones'


all_tokens=[]
word_tokens = []
punctuation = []
comma_pattern = r'(,)'
period_pattern = r'(.)'
question_pattern = r'(?)'
word_pattern = r'(\w+)'

def word_tokenize():
    tokens=[]
    text1 = input('please input your text:')
    tokens = nltk.tokenize.regexp_tokenize(text1, word_pattern)
    tokens1=[item.lower() for item in tokens]
    return (tokens1)
# tokens= nltk.regexp_tokenize(text,pattern)

def get_pron():
    phoneme=[]
    entries = nltk.corpus.cmudict.dict()
    #print(len(entries))
    for tokens1 in word_tokenize():
        try:
            words=entries[tokens1][0]
            words=[item.lower() for item in words]
            words= nltk.tokenize.regexp_tokenize(str(words), r'([a-z]{1,2})')
        except KeyError:
            input('Sorry it is wrond!')
            exit()
        phoneme.append(words)

    return (phoneme)


def get_wav(inputlist=None):
    inputlist = inputlist if inputlist is not None else []
    allfile=[]
    for root,dirs,files in os.walk(filePath):
       #for dirs in dirnames:
          #allfile.append(os.path.join(root,dir))
       for word in inputlist:
           for name in word:
               name = name + '.wav'
               allfile.append(os.path.join(name))
               #allfile.append(os.path.join(root,name))
               #print (os.path.join(root, name))

       return(allfile)

def get_word():
    print(word_tokenize())

def out_wav():
    #print(get_pron())
    allfile = get_wav(get_pron())
    return (allfile)

#get_wav(out_wav())
#def get_data(out_wav):
 #   voice_data=np.array([],dtype=None)

def playing():
    out=simpleaudio.Audio()
    voice_data = np.array([], dtype=nptype)
    for eachv in out_wav():
        out.load(eachv)
        voice_data=np.append(eachv,out.data)
    return voice_data



out=simpleaudio.Audio()
out.load(playing())
out.rescale(1.0)
out.change_speed(1.0)
out.play()

'''
def wav_data(phoneme, wavfile):
        voice_data = np.array([], dtype=nptype)
        for elements in wavfile:
            for elements1 in phoneme:
                out.load(elements1)
                voice_data = np.append(voice_data, out.data)
        return voice_data'''




'''print(wav_data(get_pron(), out_wav()))



a=simpleaudio.Audio()
a.rescale(1.0)
a.change_speed(1.0)
    # add a.data to out.data
a.play(b)
    # a.data might be [1, 4, 12, 56, ... 13]
    # a.data might be [21, 42, 122, 526, ... 13]
    # out.data need to be [1, 4, 12, 56, ..., 13, 21, 42, 122, 526, ... 13]'''

