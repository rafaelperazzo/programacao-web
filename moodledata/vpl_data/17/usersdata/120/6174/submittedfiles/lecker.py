# -*- coding: utf-8 -*-
from __future__ import division
import math
#ENTRADA
a=input('insira o primeiro valor:')
b=input('insira o segundo valor:')
c=input('insira o terceiro valor:')
d=input('insira o quarto valor:')
#SAIDA
if a>b:
    contador=contador+1
if b>c and b>a:
    contador=contador+1
if c>b and c>d:
    contador=contador+1        
if d>c:
    contador=contador+1
if contador==1:
    print('S')
else:
    print('N')


