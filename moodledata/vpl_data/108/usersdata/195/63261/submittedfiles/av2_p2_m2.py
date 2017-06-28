# -*- coding: utf-8 -*-
S=[]
x=int(input('digite a quantidade de salas:'))
for i in range(0,x,1):
    y=int(input('digite a quantidade de vidas de cada sala:'))
    S.append(y)
PE=int(input('porta de entrada:'))
PS=int(input('porta de saida:'))
soma=0
for i in range(PE,PS+1,1):
    soma=soma+S[i]
print(soma)

