import nltk
import os

'''s = ['N','IHO','K','S']
entries = nltk.corpus.cmudict.entries()
print('Example:',entries[0])
word_list = [word for word,pron in entries if pron[-4:]==s]
print(word_list)

entries = nltk.corpus.cmudict.entries()
print(len(entries)) # 133737
for entry in entries[1:300]:
    print(entry)

wav_folder= '/Users/apple/Downloads/cpslp-assignment-4/monophones'

def get_wavs():
        l=[]
        for root, dirs, files in os.walk(wav_folder, topdown=False):
            for file in files:
                if os.path.splitext(wav_folder)[1]=='.wav':
                    l.append(os.path.join(root,file))
        return l

get_wavs()'''

import os


# 遍历指定目录，显示目录下的所有文件名
def eachFile(filepath):
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s%s' % (filepath, allDir))
        print(child.decode('gbk'))  # .decode('gbk')是解决中文显示乱码问题


# 读取文件内容并打印
def readFile(filename):
    fopen = open(filename, 'r')  
    for eachLine in fopen:
        print("read：", eachLine)
    fopen.close()


# 输入多行文字，写入指定文件并保存到指定文件夹
'''def writeFile(filename):
    fopen = open(filename, 'w')
    print( "\r请任意输入多行文字", " ( 输入 .号回车保存)")
    while True:
        aLine = input()
        if aLine != ".":
            fopen.write('%s%s' % (aLine, os.linesep))
        else:
            print
            "文件已保存!"
            break
    fopen.close()'''


if __name__ == '__main__':
    filePath = '/Users/apple/Downloads/cpslp-assignment-4/monophones'
    filePathI = '/Users/apple/Downloads/cpslp-assignment-4/monophones'
    readFile(filePath)
  #filePathC = "C:\\"
  #eachFile(filePathC)

  #writeFile(filePathI)
