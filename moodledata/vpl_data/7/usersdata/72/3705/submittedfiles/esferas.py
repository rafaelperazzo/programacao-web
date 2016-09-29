# -*- coding: utf-8 -*-
from __future__ import division
#ENTRADA
a=input ('digite o peso da esfera a:')
b=input ('digite o peso da esfera b:')
c=input ('digite o peso da esfera c:')
d=input ('digite o peso da esfera d:')

#PROCESSAMENTO

if a==b+c+d and b+c==d and b==c: 
    print ('S')
else:
    print ('N')