# -*- coding: utf-8 -*-
n=int(input('digite a quantidade de salas:'))
a=[]
for i in range(1,n+1,1):
    porta=int(input('digite o valor da porta:'))
    a.append(porta)
    
x=int(input('digite a porta de entrada:'))
y=int(input('digite a porta de saída:'))
soma=0
for j in range(x,y+1,1):
    soma=soma+a[j]
print(soma)

