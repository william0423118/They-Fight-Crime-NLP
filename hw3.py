#!/usr/bin/env python
# coding: utf-8


import glob
from textblob import TextBlob
import numpy as np

def readfile():
    male = []
    female = []
    for filename in glob.glob('datafiles/*.txt'):
        if 'female' in filename.lower() or 'she' in filename.lower() or    'women' in filename.lower() or 'woman' in filename.lower():
            female.append(filename)
        else:
            male.append(filename)


    Lines = []
    for i in range (16):
        with open(male[i]) as file: # Use file to refer to the file object
            lines=[(line) for line in (file)]
            if len(lines) == 1:
                #Lines.extend(lines[0].split(','))
                pass
            else:
                Lines.extend(lines)
            
    for i,item in enumerate(Lines):
        if item[0] != 'H':
            Lines[i] = "He's " + item
        #print (item)
        
    LinesF = []
    for i in range (16):
        with open(female[i]) as file: # Use file to refer to the file object
            lines=[(line) for line in (file)]
            if len(lines) == 1:
                #Lines.extend(lines[0].split(','))
                pass
            else:
                LinesF.extend(lines)
            
    for i,item in enumerate(LinesF):
        if item[0] == 'A':
            LinesF[i] = "She's " + item
        #print (item)

    Final = Lines + LinesF
    return Final, Lines, LinesF


def sentimentalayisis(Lines, LinesF):
    polaM = []
    polaF = []
    for item in Lines:
        polaM.append(TextBlob(item).sentiment[0])
        
    for item in LinesF:
        polaF.append(TextBlob(item).sentiment[0])



    Best = Lines[np.argmax(polaM)] + LinesF[np.argmax(polaF)]# + 'They fight crime!'
    Worst = Lines[np.argmin(polaM)] + LinesF[np.argmin(polaF)] + 'They fight crime!'
    print(Best)
    print( Worst)
    return Best, Worst


def commonchar(Final):
    adj = []
    #ALL = TextBlob(Final)
    for i in range(len(Final)):
        adj.extend(Final[i].strip(' ').split(' ')[2:4])
    ADJ = ' '.join(adj)



    common = {}
    for item in ADJ.split(' '):
        if item in common:
            common[item] += 1
        else:
            common[item] = 1
    topn = sorted(common.items(), key=lambda x: x[1], reverse = True)
    for i in range (10):
        print (topn[i][0], topn[i][1])
    return topn

if __name__ == "__main__":
    Final, Lines, LinesF = readfile()
    Best, Worst = sentimentalayisis(Lines, LinesF)
    topn = commonchar(Final)





