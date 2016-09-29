# -*- coding: utf-8 -*-
from __future__ import division

#Entrada

p1= input ('Digite o peso da criança do lado esquerdo:')
c1= input ('Digite o valor do comprimento do lado esquerdo da gangorra:')
p2= input ('Digite o peso da criança do lado direito:')
c2= input ('Digite o valor do comprimentp do lado direito da gangorra:')

#Processameno e Saida

e1=p1*c1
e2=p2*c2

if (e1==e2):
    print ('0')
elif (c2>c1):
    print ('-1')
else:
    print ('1')


