import pandas as pd
import numpy as np
import os.path
import struct

filePath = 'C:/Users/ss/Desktop/mfinal/npy/'
filePath1 = 'C:/Users/ss/Desktop/mfinal/csv/'
fileAll = os.listdir(filePath)

for file in fileAll:
       a = np.load(filePath + file)
       a1 = np.savetxt(filePath1 + file[:-4] +'.csv',a,fmt='%7f', delimiter=",")

filePath2 = 'C:/Users/ss/Desktop/mfinal/csv/'
fileAll2 = os.listdir(filePath2)
os.makedirs(filePath2+'./txt')
for file1 in fileAll2:
    b = pd.read_csv(filePath2 + file1, header=None)
    b1 = b.iloc[:, [0, 1, 2, 3]]
    b1.to_csv(filePath2+'/txt/'+ file1[:-4] + '.txt', sep=' ',index=False, header=False)

os.makedirs(filePath2+'./bin')
dirroot = r"C:/Users/ss/Desktop/mfinal/csv/txt/"
newdirroot= r"C:/Users/ss/Desktop/mfinal/csv//bin/"

for dirnames in os.listdir(dirroot):
    if dirnames.split('.')[-1]!='txt':
        continue

    bin_filename=dirnames.split('.txt')[0] +'.bin'

    txt_file=open(dirroot + dirnames,'r')
    bin_file=open(newdirroot + bin_filename,'wb')

    lines=txt_file.readlines()
    for j,line in enumerate(lines):
        if j == 0:
            continue
        curLine=line.split(' ')[0:3]
        curLine.append(line.split(' ')[3])

        for i in range(len(curLine)):
            if len(curLine[i])==0:
                continue
            if i == 3:
                parsedata = struct.pack("f",float(curLine[i]))

                bin_file.write(parsedata)
            else:
                parsedata = struct.pack("f",float(curLine[i]))
                bin_file.write(parsedata)

    bin_file.close()
    txt_file.close()