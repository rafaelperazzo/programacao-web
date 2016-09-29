# -*- coding: utf-8 -*-
from __future__ import division
import math

a=int(input('Digite o primeiro valor: '))
b=int(input('Digite o segundo valor: '))
c=int(input('Digite o terceiro valor: '))
d=int(input('Digite o quarto valor: '))

if a==b and a==c and a==d:
    print ('N')
    
else:
    if a>b or (b>c and b>a) or (c>b and c>d) or d>c:
        print ('S')