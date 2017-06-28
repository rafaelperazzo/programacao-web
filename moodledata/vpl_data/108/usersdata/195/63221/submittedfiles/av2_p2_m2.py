# -*- coding: utf-8 -*-
x=quantidade de salas
y=quantidade de vidas por sala
S=[]
x=int(input('digite x:'))
for i in range(0,x,1):
    y=int(input('digite y:'))
    S.append(y)
PE=int(input('porta de entrada:'))
PS=int(input('porta de saida:'))
soma=0
for i in range(PE,PS+1,1):
    soma=soma+1
print(soma)

