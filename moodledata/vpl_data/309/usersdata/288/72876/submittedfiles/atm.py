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
    print z//20
elif (z%5)==0:
    print z//5
    print z//10
elif (z%2)==0:
    print z//2
    print z//5
elif (z%1)==0:
    print z//1
    print z//2

       

       
