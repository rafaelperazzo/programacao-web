# -*- coding: utf-8 -*-
import math
n= int(input('digite um valor de n par:'))
x1= int(input('digite a coordenada x da primeira figurinha:'))
y1= int(input('digite a coordenada y da primeira figurinha:'))
x2= int(input('digite a coordenada x da segunda figurinha:'))
y2= int(input('digite a coordenada y da segunda figurinha:'))

if y1 <=n/2 and y2>n/2:
    print ('s')
if x1 <=n/2 and x2>n/2:
    print ('s')
else:
    print('n')
