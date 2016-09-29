# -*- coding: utf-8 -*-
from __future__ import division

p1=input('Peso da criança da esquerda: ')
c1=input('Comprimento esquerdo: ')
p2=input('Peso da criança da direita: ')
c2=input('Comprimento direito: ')

if (p1*c1) > (p2*c2):
    print ('-1')

elif (p1*c1) < (p2*c2):
    print ('1')
    
else:
    print ('0')