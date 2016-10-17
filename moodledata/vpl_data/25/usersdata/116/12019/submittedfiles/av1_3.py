# -*- coding: utf-8 -*-
from __future__ import division
import math

a = input ('insira o valor de a:')
b = input ('insira o valor de b:')

if a>=b:
    c=a%b
    cont=0
    while c>0:
        c=a%b
        cont = cont +1
        a=b
        b=c
    print (a)
    print (cont)
if b>a:
    c=b%a
    cont=0
    while c>0:
        c=b%a
        cont = cont+1
        b=a
        a=c
        print (b)
        print (cont)
