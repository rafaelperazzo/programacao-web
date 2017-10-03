# -*- coding: utf-8 -*-
import math

n=int(input('Digite n : '))
Soma=0
contador=0
numerador=1
i=0
if(n<0):
    n=-1*n

while(contador<n):
    Soma= Soma + numerador/(n-i)
    i=i+1
    contador=contador +1
    numerador= numerador+1

print('%.5f'%Soma)