# -*- coding: utf-8 -*-
from __future__ import division
import math
n= int(input('Digite o valor de n: '))
x1= int(input('Digite o valor de x1: '))
y1= int(input('Digite o valor de y1: '))
x2= int(input('Digite o valor de x2: '))
y2= int(input('Digite o valor de y2: '))

    
q= n//2

for i in range (1, q+1, 1):
    if x1==i:
        x1=0
for i in range (q+1, n+1, 1):
    if x1==i:
        x1=-3


for i in range (1, q+1, 1):
    if y1==i:
        y1=0
for i in range (q+1, n+1, 1):
    if y1==i:
        y1=1


for i in range (1, q+1, 1):
    if x2==i:
        x2=0
for i in range (q+1, n+1, 1):
    if x2==i:
        x2=-3
    
for i in range (1, q+1, 1):
    if y2==i:
        y2=0
for i in range (q+1, n+1, 1):
    if y2==i:
        y2=1

if (x1+y1)==(x2+y2):
    print('N')
else:
    print('S')