# -*- coding: utf-8 -*-
from __future__ import division
#ENTRADA
p1=input ('digite o peso da criança do lado esquerdo:')
c1=input ('digite o comprimento do lado esquerdo da gangorra:')
p2=input ('digite o peso da criança do lado direito:')
c2=input ('digite o comprimento do lado direito da gangorra:')

#SAIDA
if (p1*c1)=(p2*c2):
    print ('ZERO')
elif p1<=p2:
    print ('MENOS UM')
else p2>=p1:
    print ('UM')
