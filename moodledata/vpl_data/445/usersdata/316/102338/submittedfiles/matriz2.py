# -*- coding: utf-8 -*-
import numpy as np
tm=int(input('Digite a dimensão da matriz quadrada: '))
n=[]
for i in range(0,tm,1):
    m=[]
    for j in range(0,tm,1):
        m.append(float(input('Digite o valor da linha%d e da coluna%d: ' %((j+1),(i+1)))))
    n.append(m)
print(n)
l1=n[0][0]+n[0][1]+n[0][2]
l2=n[1][0]+n[1][1]+n[1][2]
l3=n[2][0]+n[2][1]+n[2][2]

c1=n[0][0]+n[1][0]+n[2][0]
c2=n[0][1]+n[1][1]+n[2][1]
c3=n[0][2]+n[1][2]+n[2][2]

dp=n[0][0]+n[1][1]+n[2][2]

ds=n[0][2]+n[1][1]+n[2][0]


    