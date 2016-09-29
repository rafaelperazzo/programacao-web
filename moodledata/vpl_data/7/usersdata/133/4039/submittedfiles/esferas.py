# -*- coding: utf-8 -*-
from __future__ import division
print('Programa que verifica se quatro esferas estão em equilíbro.')
a=input('Digite o valor da esfera a:')
b=input('Digite o valor da esfera b:')
c=input('Digite o valor da esfera c:')
d=input('Digite o valor da esfera d:')
if((a==b+c+d)and(b+c==d)and(b==c)):
    print('S')
else:
    print('N')
