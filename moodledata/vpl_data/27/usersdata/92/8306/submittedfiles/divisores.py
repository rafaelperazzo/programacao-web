# -*- coding: utf-8 -*-
from __future__ import division
import math

n= int(input('Digite o valor de n: '))
a= int(input('Digite o primeiro valor: '))
b= int(input('Digite o segundo valor: '))

c=1
i=1

while i<=n:

    if c%a!=0 and c%b!=0:
        c=c+1
    
    else:
        print(c)
        i=i+1
        c=c+1