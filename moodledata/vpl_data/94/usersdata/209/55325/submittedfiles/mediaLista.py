# -*- coding: utf-8 -*-

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
print(conjunto)