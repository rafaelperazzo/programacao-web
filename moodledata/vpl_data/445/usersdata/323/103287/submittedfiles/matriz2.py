# -*- coding: utf-8 -*-

import numpy as np

z = int(input('Digite a dimensão da matriz(i=j): '))
m = []
for i in range(0,z,1):
    n=[]
    for j in range(0,z,1):
        n.append(float(input('Digite o valor da linha%d e da coluna%d: '%((j+1),(i+1)))))
    m.append(n)
if z<=2:
    med1=0
    med1=med1+m[0][0]+m[0][1]
    med1=med1/2.0
    med2=0
    med2=med2+m[0][0]+m[1][1]
    med2=med2/2.0
    if med1!=med2:
        print('N')
    else:
        print('S')
else:
    med1=0
    for i in range(0):
        for j in range(0,z,1):
            med1=med1+m[i][j]
    med1=med1/3
    med2=0
    for i in range(1):
        for j in range(0,z,1):
            med2=med2+m[i][j]
    med2=med2/3
    med3=0
    for i in range(2):
        for j in range(0,z,1):
            med3=med3+m[i][j]
    med3=med3/3
    if med1==med2 and med2==med3 and med1==med3:
        print('N')
    else:
        print('S')