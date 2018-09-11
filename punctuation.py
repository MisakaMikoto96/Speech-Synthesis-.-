import re
from nltk.corpus import cmudict


def insertsilence():
    tokens = []
    punctuation = []
    word_pattern = r'(\w+)'
    comma_pattern = r'(,)'
    period_pattern = r'(.)'
    question_pattern = r'(?)'

    text=input('please input:')
    result1 = re.sub(r'[^a-zA-Z0-9 ,.?]', '', text)  # remove all characters we don't want
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

        print(phone_sequence)
