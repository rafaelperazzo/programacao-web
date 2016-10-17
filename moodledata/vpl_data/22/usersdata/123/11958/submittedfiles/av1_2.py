# -*- coding: utf-8 -*-
from __future__ import division
import math
l= int(input('Insira o primeiro número da sequência:'))
f= int(input('Insira o segundo número da sequência:'))
d= int(input('Insira o terceiro número da sequência:'))
c= int(input('Insira o quarto número da sequência:'))
if (l==d) and (l!=f) and (f!=d) and (d!=c):
    print('V')
elif (f==c) and (l!=f) and (f!=d) and (d!=c):
    print ('V')
else:
    print('F')