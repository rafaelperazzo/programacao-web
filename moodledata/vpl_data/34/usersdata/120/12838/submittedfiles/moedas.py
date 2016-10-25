# -*- coding: utf-8 -*-
from __future__ import division
#Entrada
a=int(input('insira o valor de a:'))
b=int(input('insira o valor de b:'))
c=int(input('insira o valor de c:'))

#Processamento
if a<b: 
    c//a
    (c%a)//b
else:
    c//b
    (c%b)//b