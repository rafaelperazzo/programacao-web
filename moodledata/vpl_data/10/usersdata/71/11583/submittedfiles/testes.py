# -*- coding: utf-8 -*-
from __future__ import division

b = input('INSIRA O NUMERO: ')
a = b
n=1

while a//10!=0:
    n=n+1
    a=a//10
    
print n
    