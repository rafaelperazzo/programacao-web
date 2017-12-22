# -*- coding: utf-8 -*-
import math
n= int(input('digite o valor de múultiplos:'))
a= int(input('digite a:'))
b= int(input('digite b:'))
numeroteste=1
contador=0

while (contador<n):
    if(numeroteste%a)==0 or (numeroteste%b)==0:
        print(numeroteste)
        numeroteste= numeroteste+1
        contador= contador+1
    else:
        numeroteste= numeroteste+1