# -*- coding: utf-8 -*-
from __future__ import division
import math
#entrada
n=input('digite a quantidade de numeros a serem mostrados:') 
a=input('digite o valor de a:')
b=input('digite o valor de b:')
i=2
contador=0
#processamento e saida 
while contador<n:
    if i%a==0 or i%b==0:
        print(i)
        contador=contador+1
    i=i+1