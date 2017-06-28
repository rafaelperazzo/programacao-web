# -*- coding: utf-8 -*-
n=int(input('digite n:'))
L=[]
for i in range(0,n,1):
    valor=int(input('digite o valor:'))
    L.append(valor)
portaE=int(input('digite a porta de entrada:'))
portaS=int(input('digite a porta de saida:'))
soma=0
for i in range(portaE,portaS+1,1):
    soma=soma+L[i]
print(soma)