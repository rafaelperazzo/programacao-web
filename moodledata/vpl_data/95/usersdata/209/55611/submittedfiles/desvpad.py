# -*- coding: utf-8 -*-
import math

#comece abaixo
def dp(n):
    somatorio=0
    for i in range(0,n,1):
        somatorio=somatorio+(conjunto[i]-media)**2
    dp=((1/(n-1))*somatorio)**0.5
    print('%.2f'%dp)
conjunto=[]
soma=0
n=int(input('Digite o valor de n:'))
for i in range(0,n,1):
    X=float(input('Digite o valor:'))
    conjunto.append(X)
    soma=soma+X
media=soma/n
print('%.2f'%conjunto[0])
print('%.2f'%conjunto[n-1])
print('%.2f'%media)
dp(n)