# -*- coding: utf-8 -*-
import math

#comece abaixo

n= int(input('Digite a quantidade de valores n da lista:'))
L=[]
SOMA=0
MEDIA=0
SOMATORIO=0
for i in range(0,n,1):
    a= float(input('Digite o valor da lista:'))
    L.append(a)
    SOMA= SOMA+a
MEDIA = SOMA/n
for i in range(0,n,1):
    SOMATORIO= SOMATORIO + (L[i]-MEDIA)**2

S= ((1/n-1)*SOMATORIO)**(1/2)

print(L[0])
print(L[i-1])
print(MEDIA)
print(L)
print(S)


