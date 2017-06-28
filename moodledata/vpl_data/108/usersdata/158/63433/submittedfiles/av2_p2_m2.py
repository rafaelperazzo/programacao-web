# -*- coding: utf-8 -*-
n=int(input(digite a quantidades de salas)
s=[]
for i in range (1,n+1,1):
    p=int(input('digite o numero p:'))
    s.append(p)
x=int(input('digite porta de entrada:'))
y=int(input('digite porta de saída:'))
soma=0
for j in range(x,y+1,1):
    soma=soma+s[j]
print(soma)