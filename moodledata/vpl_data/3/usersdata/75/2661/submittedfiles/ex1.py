# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#Processamento 

delta=(b**2)-(4*a*c)
if (delta>=0):
    x1=(-b+((delta)**1/2))/2a
    x2=(-b-((delta)**1/2))/2a
    print ('%.2f'%(x1))
    print ('%.2f'%(x2))
else (delta<0):
    print ('SRR')
    
