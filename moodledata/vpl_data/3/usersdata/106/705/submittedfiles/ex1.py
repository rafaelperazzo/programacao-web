# -*- coding: utf-8 -*-
from __future__ import division

#entrada
a = input ('Digite um valor para a: ')
b = input ('Digite um valor para b: ')
c = input ('Digite um valor para c: ')
#processamento e saída:
if a>b and a>c:
    print ('%.2f' %a)
if b>c and b>a:
    print ('%.2f' %b)
if c>a and c>b:
    print ('%.2f' %c)