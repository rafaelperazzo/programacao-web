# -*- coding: utf-8 -*-
from __future__ import division
#entrada
a = input ('Digite um valor para a:')

#processamento
if a>=0:
    b= (a**0.5)
    print ('%.2f' %b)
if a<0:
    b= (a**2)
    print ('%.2f' %b)
