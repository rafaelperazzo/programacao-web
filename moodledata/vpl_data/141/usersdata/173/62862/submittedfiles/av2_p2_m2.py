# -*- coding: utf-8 -*-
n=int(input('Digite a quantidade de salas: '))
a=[]
for i in range(1,n+1,1):
    a.append(int(input('Digite a quantidade de vidas: ')))
x=int(input('Digite a porta de entrada: '))
y=int(input('Digite a porta de saída: '))
soma=0
for i in range(x,y+1,1):
    soma=soma+a[i]
print(soma)