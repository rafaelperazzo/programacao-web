# -*- coding: utf-8 -*-
import math
n=int(input('digite a quantidade de divisores a serem mostrados:'))
a=int(input('digite o numero 1:'))
b=int(input('digite o numero 2:'))
contador=0
i=1
while contador<n:
    if i%a==0 or i%b==0:
        print(i)
        contador=contador+1
    i=i+1
        
