# -*- coding: utf-8 -*-
import numpy as np
tm=int(input('Digite a dimensão da matriz quadrada: '))
n=[]
for i in range(0,tm,1):
    m=[]
    for j in range(0,tm,1):
        m.append(float(input('Digite o valor da linha%d e da coluna%d: ' %((j+1),(i+1)))))
    n.append(m)

media=0
for i in range(tm[1]):
    for j in range(tm):
        media=media+n[i][j]
media=media/3
print(media)

    