# -*- coding: utf-8 -*-
from __future__ import division
import math

a = input ('insira o valor de a:')
b = input ('insira o valor de b:')
c=1
cont=0
if a>=b:
    while c>0:
        c=a%b
        cont = cont +1
        a=b
        b=c
    print (a)
    print (cont)
else:
    
    while c>0:
        c=b%a
        cont = cont+1
        b=a
        a=c
    print (b)
    print (cont)
