# -*- coding: utf-8 -*-
import math
n=int(input('digite a dimensão da barra de chocolate seu cuzão:'))
x1=int(input('digite a coordenada x da figura 1:'))
y1=int(input('digite a coordenada y da figura 1:'))
x2=int(input('digite a coordenada x da figura 2:'))
y2=int(input('digite a coordenada y da figura 2:'))

if x1<=(n/2) and y1<=(n/2) and x2>=(n/2) and y2>=(n/2) or x2<=(n/2) and y2<=(n/2) and x1>=(n/2) and y1>=(n/2):
    print('S')
else:
    print('N')









