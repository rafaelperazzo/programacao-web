# -*- coding: utf-8 -*-
    
n=int(input('digite a quantidade de salas:'))

for i in range(0,n,1):
    a=[]
    m=float(input('digite a quantidade de vidas da sala:'))
    a.append(m)
    
b=int(input('digite o número da porta de entrada:'))
c=int(input('digite o numero da porta de saida:'))
soma=0
for i in range(b,c+1,1):
    soma=soma+a[i]
print(soma)
