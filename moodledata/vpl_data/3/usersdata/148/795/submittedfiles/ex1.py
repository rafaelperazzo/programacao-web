# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite um numero:')
b = input('Digite outro numero:')
c = input('Digite outro numero:')
#PROCESSAMENTO
if a>=b and a>=c :
    print('%.2f' %a)
elif b>=a and b>=c :
    print('%.2f' %b)
elif c>=a and c>=b :
    print('%.2f' %c)
