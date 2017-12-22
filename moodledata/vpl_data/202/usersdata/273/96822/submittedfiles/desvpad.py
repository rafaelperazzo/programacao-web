# -*- coding: utf-8 -*-
import math

#comece abaixo

list=[]
n=int(input('digite a quantidade de valores: '))
i=0
soma=0

for i in range (0,n,1):
    numero=float(input('digite um numero: '))
    list.append(numero)
    soma=soma+numero

media=soma/n
somatorio=0
for l in range(0,n,1):
    somatorio=somatorio+((list[l]-media)**2)

desvio=((1)/(n-1))*(somatorio)

print('%.2f'% list[0])
print('%.2f'% list[n-1])
print('%.2f'% media)
print('%.2f'% desvio)






    
