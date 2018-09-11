import os

def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        print(root) #当前目录路径
        print(dirs) #当前路径下所有子目录
        print(files) #当前路径下所有非目录子文件

def file_name1(file_dir):
    L=[]
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.jpeg':
                L.append(os.path.join(root, file))
    return L

file_name1('monophones')

import os,re
filenames = os.listdir(os.getcwd())
filenames_bak = []
for name in filenames:
    ok = re.search(r'\.rmvb$',name)
    if ok:filenames_bak.append(name[:-5])
f = open("names.txt","w")
for name in filenames_bak:
    f.write(name+'\n')
f.close()

file_lst = []
for path, dir, files in os.walk('./'):
    file_lst += files
file_count = len(file_lst) * 1.0
for key, lst in groupby(file_lst, key=lambda x: os.path.splitext(x)[0]):
    if cmp(key, 'tvmticket') == 0:
      pass