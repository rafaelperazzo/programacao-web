# -*- coding: utf-8 -*-
from __future__ import division
#ENTRADA:
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')

#PROCESSAMENTO:
Delta = b**2 - (4*a*c)

x1=(-b+(Delta)**0.5)/(2*a)
x2=(-b-(Delta)**0.5)/(2*a)

#SAIDA:
if Delta>=0:
   print (x1)
   print (x2)
   
else :
    print ('SRR')