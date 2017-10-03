# -*- coding: utf-8 -*-
import math
n = int(input('digite a quantidade de termos: '))
a = int(input('digite o valor de a: '))
b = int(input('digite o valor de b: '))
numeroteste=1
contador=0
while (contador<n):
    if (numeroteste%a==0) or (numeroteste==0):
        print(numeroteste)
        numeroteste=numeroteste + 1
        contador=contador+1
    else :
        numeroteste=numeroteste+1
