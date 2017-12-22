# -*- coding: utf-8 -*-
import math

#comece abaixo

list=[]
n=int(input('digite a quantidade de valores: '))
i=0
soma=0

for i in range (i,n,1):
    numero=int(input('digite um numero: '))
    list.append(numero)
    soma=soma+numero

media=soma/n
somatorio=0
for i in range(i,n-1,1):
    somatorio=somatorio+((a[i]-media)**2)
desvio=((1)/(n-1))*(somatorio)
print('%.2f'% list[0])
print('%.2f'% list[n-1])
print('%.2f'% media)
print('%.2f'% desvio)





    
