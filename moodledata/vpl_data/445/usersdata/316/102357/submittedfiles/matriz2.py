# -*- coding: utf-8 -*-
import numpy as np
tm=int(input('Digite a dimensão da matriz quadrada: '))
n=[]
for i in range(0,tm,1):
    m=[]
    for j in range(0,tm,1):
        m.append(int(input('Digite o valor da linha%d e da coluna%d: ' %((j+1),(i+1)))))
    n.append(m)
if tm<=2:
    media=0
    for i in range(0):
        for j in range(tm):
            media=media+n[i][j]
    media=media/2
    print(media)
    #linha_2
    media=0
    for i in range(1):
        for j in range(tm):
            media=media+n[i][j]
    media=media/2
    print(media)
else:
    media=0
    for i in range(0):
        for j in range(tm):
            media=media+n[i][j]
    media=media/3
    print(media)
    #linha_2
    media=0
    for i in range(1):
        for j in range(tm):
            media=media+n[i][j]
    media=media/3
    print(media)
    #linha_3
    media=0
    for i in range(2):
        for j in range(tm):
            media=media+n[i][j]
    media=media/3
    print(media)
    
    
    

    