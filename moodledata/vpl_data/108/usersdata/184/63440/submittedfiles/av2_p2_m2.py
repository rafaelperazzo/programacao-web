# -*- coding: utf-8 -*-
n=int(input('digite a quantidades de sala:'))
x=[]
for i in range (1,n+1,1):
    porta=int(input('digite o número da porta:'))
    x.append(porta)
y=int(input('digite a porta de entrada:'))
z=int(input('digite a porta de saida:'))
soma=0
for j in range(y,z+1,1):
    soma=soma+x[j]
print(soma)


