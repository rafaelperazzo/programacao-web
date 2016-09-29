# -*- coding: utf-8 -*-
from __future__ import division
#ENTRADA
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#PROCESSAMENTO
delta=(b**2)-4*a*c
#SAIDA
if delta>=0:
    x1=((-b)+(delta**0.5))/(2*a)
    x2=((-b)-(delta**0.5))/(2*a)
    print ('x1=%.2f' %x1)
    print ('x2=%.2f' %x2)
else : 
    print ('SRR')

