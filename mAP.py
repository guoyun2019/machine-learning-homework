import numpy as np
import pandas as pd
import string
import re
import os
import string
import math

test = pd.read_csv('box_coordinate.csv',header=-1)
test=np.array(test)
#f = np.loadtxt("coreless_battery00001369.txt"，encoding='utf-8')
#f = open("coreless_battery00001369.txt",encoding='utf-8')
#str = f.read()
#str1=str.split() 
core=[]
coreless=[]
for i in range(np.shape(test)[0]):
    print(i,'\n')
    core_num=0
    coreless_num=0
    core_num_real=0
    coreless_num_real=0
    if(test[i][1]==' Class: core_battery'):
        core_num=core_num+1
    if(test[i][1]==' Class: coreless_battery'):
        coreless_num=coreless_num+1
    if(test[i][6]==' Class: core_battery'):
        core_num=core_num+1
    if(test[i][6]==' Class: coreless_battery'):
        coreless_num=coreless_num+1
    if(test[i][11]==' Class: core_battery'):
        core_num=core_num+1
    if(test[i][11]==' Class: coreless_battery'):
        coreless_num=coreless_num+1
    if(test[i][16]==' Class: core_battery'):
        core_num=core_num+1
    if(test[i][16]==' Class: coreless_battery'):
        coreless_num=coreless_num+1

    if(type(test[i][2])==float):
        continue
    if(type(test[i][6])==float):
        print('case1')
        num=test[i][5][17:25]
        path="coreless_battery%s.txt"%num
        if(os.path.exists(path)):
            path="coreless_battery%s.txt"%num
        else :
            path="core_battery%s.txt"%num
        f = open(path,encoding='utf-8')
        str = f.read().split()
        for j in range(len(str)):
            if(str[j]=='不带电芯充电宝'):
                coreless_num_real=coreless_num_real+1
            if(str[j]=='带电芯充电宝'):
                core_num_real=core_num_real+1
        if(core_num>=core_num_real and core_num_real!=0):
            core_p=1
            core.append(core_p)
        if(core_num<core_num_real and core_num_real!=0):
            core_p=(float(core_num)/float(core_num_real))
            core.append(core_p)
        if(coreless_num>=coreless_num_real and coreless_num_real!=0):
            coreless_p=1
            coreless.append(coreless_p)
        if(coreless_num<coreless_num_real and coreless_num_real!=0):
            coreless_p=(float(coreless_num)/float(coreless_num_real))
            coreless.append(coreless_p)
    elif(type(test[i][11])==float):
        num=test[i][10][17:25]
        path="coreless_battery%s.txt"%num
        if(os.path.exists(path)):
            path="coreless_battery%s.txt"%num
        else:
            path="core_battery%s.txt"%num
        f = open(path,encoding='utf-8')
        str = f.read().split()
        for j in range(len(str)):
            if(str[j]=='不带电芯充电宝'):
                coreless_num_real=coreless_num_real+1
            if(str[j]=='带电芯充电宝'):
                core_num_real=core_num_real+1
        if(core_num>=core_num_real and core_num_real!=0):
            core_p=1
            core.append(core_p)
        if(core_num<core_num_real and core_num_real!=0):
            core_p=(float(core_num)/float(core_num_real))
            core.append(core_p)
        if(coreless_num>=coreless_num_real and coreless_num_real!=0):
            coreless_p=1
            coreless.append(coreless_p)
        if(coreless_num<coreless_num_real and coreless_num_real!=0):
            coreless_p=(float(coreless_num)/float(coreless_num_real))
            coreless.append(coreless_p)
    elif(type(test[i][16])==float):
        num=test[i][15][17:25]
        path="coreless_battery%s.txt"%num
        if(os.path.exists(path)):
            path="coreless_battery%s.txt"%num
        else:
            path="core_battery%s.txt"%num
        f = open(path,encoding='utf-8')
        str = f.read().split()
        for j in range(len(str)):
            if(str[j]=='不带电芯充电宝'):
                coreless_num_real=coreless_num_real+1
            if(str[j]=='带电芯充电宝'):
                core_num_real=core_num_real+1
        if(core_num>=core_num_real and core_num_real!=0):
            core_p=1
            core.append(core_p)
        if(core_num<core_num_real and core_num_real!=0):
            core_p=(float(core_num)/float(core_num_real))
            core.append(core_p)
        if(coreless_num>=coreless_num_real and coreless_num_real!=0):
            coreless_p=1
            coreless.append(coreless_p)
        if(coreless_num<coreless_num_real and coreless_num_real!=0):
            coreless_p=(float(coreless_num)/float(coreless_num_real))
            coreless.append(coreless_p)
    else :
        num=test[i][20][17:25]
        path="coreless_battery%s.txt"%num
        if(os.path.exists(path)):
            path="coreless_battery%s.txt"%num
        else:
            path="core_battery%s.txt"%num
        f = open(path,encoding='utf-8')
        str = f.read().split()
        for j in range(len(str)):
            if(str[j]=='不带电芯充电宝'):
                coreless_num_real=coreless_num_real+1
            if(str[j]=='带电芯充电宝'):
                core_num_real=core_num_real+1
        if(core_num>=core_num_real and core_num_real!=0):
            core_p=1
            core.append(core_p)
        if(core_num<core_num_real and core_num_real!=0):
            core_p=(float(core_num)/float(core_num_real))
            core.append(core_p)
        if(coreless_num>=coreless_num_real and coreless_num_real!=0):
            coreless_p=1
            coreless.append(coreless_p)
        if(coreless_num<coreless_num_real and coreless_num_real!=0):
            coreless_p=(float(coreless_num)/float(coreless_num_real))
            coreless.append(coreless_p)
core_ap=np.mean(core)
coreless_ap=np.mean(coreless)
