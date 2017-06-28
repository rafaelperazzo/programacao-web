# -*- coding: utf-8 -*-

v=int(input('escreva a quantidade de portas:'))
l=int(input('escreva a porta da entrada:'))
s=int(input('escreva a saída:'))
i=[]
for i in range(0,v,1):
    m=int(input('escreva a vida:'))
    p.append(m)
soma=0
for i in range(l,s+1,1):
    soma=soma+p[i]
print(soma)
