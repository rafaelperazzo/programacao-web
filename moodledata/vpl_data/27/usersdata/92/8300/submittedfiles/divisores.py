# -*- coding: utf-8 -*-
from __future__ import division
import math

n= int(input('Digite o valor de n: '))
a= int(input('Digite o primeiro valor: '))
b= int(input('Digite o segundo valor: '))

c=1

for i in range (1, n+1, 1):

    if c%a!=0 and c%b!=0:
        i=i-1
        c=c+1
    
    elif c%a==0 or c%b==0:
        print(c)
        c=c+1