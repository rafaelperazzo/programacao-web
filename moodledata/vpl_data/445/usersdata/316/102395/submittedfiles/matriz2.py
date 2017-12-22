# -*- coding: utf-8 -*-
import numpy as np
tm=int(input('Digite a dimensão da matriz quadrada: '))
n=[]
for i in range(0,tm,1):
    m=[]
    for j in range(0,tm,1):
        m.append(float(input('Digite o valor da linha%d e da coluna%d: ' %((j+1),(i+1)))))
    n.append(m)
if tm<=2:
    media1=0
    media1=media1+n[0][0]+n[0][1]
    media1=media1/2.0
    #linha_2
    media2=0
    media2=media2+n[1][0] +n[1][1]
    media2=media2/2.0
    if media1!=media2:
        print('n')
    else:
        print('s')
else:
    media1=0
    for i in range(0):
        for j in range(0,tm,1):
            media1=media1+n[i][j]
    media1=media1/3
    #linha_2
    media2=0
    for i in range(1):
        for j in range(0,tm,1):
            media2=media2+n[i][j]
    media2=media2/3
    #linha_3
    media3=0
    for i in range(2):
        for j in range(0,tm,1):
            media3=media3+n[i][j]
    media3=media3/3
    if media1==media2 and media2==media3 and media1==media3:
        print('n')
    else:
        print('s')
    
    
    

    