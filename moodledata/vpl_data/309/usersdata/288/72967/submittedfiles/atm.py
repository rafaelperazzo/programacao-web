# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
valor=int(input("digite o valor a ser sacado: "))

a=(valor//20)
z=(valor%20)
print a
b=(z//10)
if (z%10)==0:
    print b
else:
    print z//20
if (z%5)==0:
    print z//5
else:
    print z//10
if (z%2)==0:
    print z//2
else:
    print z//5
if (z%1)==0:
    print z//1

       

       
