import nltk
import re
from nltk.corpus import cmudict
import simpleaudio
import os
import re



filePath='/Users/apple/Downloads/cpslp-assignment-4/monophones'

pattern = r'(\w+)'

def word_tokenize():
    tokens=[]
    text1 = input('please input your text:')
    tokens = nltk.tokenize.regexp_tokenize(text1, pattern)
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
            input('Please change your input:')
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
    return allfile




'''def play_wav():

    for need_wave in get_wav:

        #a = simpleaudio.load("need_wave")
        print(need_wave)'''


'''def getallfiles(filepath):
    allfile=[]
    for root,dirs,files in os.walk(filePath):
       for dir in dirs:
          allfile.append(os.path.join(root,dir))
       for name in files:
          allfile.append(os.path.join(root, name))
    return allfile
'''

'''def main():
    filePath = '/Users/apple/Downloads/cpslp-assignment-4/monophones'
    allfile = getallfiles(filePath)
    for file in allfile:
        name = get_pron()
        print(file)

if __name__ == '__main__':
    filePath = '/Users/apple/Downloads/cpslp-assignment-4/monophones'
    allfile=getallfiles(filePath)
    for file in allfile:
       name=get_pron()
       print (file)
'''
def get_word():
    print(word_tokenize())

def out_wav():
    #print(get_pron())
    allfile = get_wav(get_pron())
    for line in allfile:
        return(allfile)

for eachv in out_wav():
    a=simpleaudio.Audio()
    a.load(str(eachv))
    a.rescale(0.9)
    a.change_speed(1.0)
    a.play()

get_wav(out_wav())





get_pron()
out_wav()