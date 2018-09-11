import os
import simpleaudio
import argparse
from nltk.corpus import cmudict
import re
import nltk

def fun2():
    input_text = input("please input your text:")
    text1=input_text.split(' ')
    return text1


def tokenize():
    text=fun2()
    pattern = r'(\w+)'
    tokens = nltk.tokenize.regexp_tokenize(text, pattern)
    # tokens= nltk.regexp_tokenize(text,pattern)
    return tokens

input()




