# -*- coding: utf-8 -*-
import math
n=int(input('Digite a quatidade de divisores a ser mostrados: '))
a=int(input('Digite o primeiro valor: '))
b=int(input('Digite o segundoo valor: '))
cont=0
e=0
for i in range(1,n+1,1):
   c=a*i
   d=b*i
   cont=cont+c
   e=e+d
    print(cont)
    print(e)