# -*- coding: utf-8 -*-
from __future__ import division

a=input('Digite aqui o peso da Esfera a:')
b=input('Digite aqui o peso da Esfera b:')
c=input('Digite aqui o peso da Esfera c:')
d=input('Digite aqui o peso da Esfera d:')

if(a==b+c+d)and(b+c==d)and(b==c):
    print('S')
    
else:
    print('N')
