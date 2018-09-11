import os

filePath = '/Users/apple/Downloads/cpslp-assignment-4/monophones'


def getallfiles(inputlist=None):
    inputlist = inputlist if inputlist is not None else []
    allfile=[]
    for root,dirnames,filenames in os.walk(filePath):
       #for dir in dirnames:
          #allfile.append(os.path.join(root,dir))
       for word in inputlist:
           for name in word:
               name = name + '.wav'
               allfile.append(os.path.join(root,name))
               #print (os.path.join(root, name))
    return allfile

if __name__ == '__main__':
    filePath = '/Users/apple/Downloads/cpslp-assignment-4/monophones'
    allfile=getallfiles([['hh','ow']])
    for file in allfile:
       print (file)