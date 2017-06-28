# -*- coding: utf-8 -*-
Q=int(input('Digite a quantidade de portas: '))
e=int(input('Digite a porta de entrada: '))
s=int(input('Digite a porta de saida: '))
a=[]
for i in range(0,q,1):
    l=int(input('Digite a quantidade de vida: '))
    a.append(l)
soma=0
for i in range(e,s+1,1):
    soma=soma+a[i]
print(soma)


