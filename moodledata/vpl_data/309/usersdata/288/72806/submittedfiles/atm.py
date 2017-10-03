# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
valor=int(input("digite o valor a ser sacado: "))
a=(valor/20)
z=(valor%20)
if valor>= 20:
    print ("%d" a)
    b=(z/10)
    if (z%10)==0:
        print b
        c=(z/5)
    elif (z%5)==0:
        print c
        d=(z/2)
    elif (z%2)==0:
        print d
        e=(z/1)
    elif (z%1)==0:
        print e
       

       
