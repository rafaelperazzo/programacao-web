# -*- coding: utf-8 -*-
Q=int(input('Digite a quantidade de portas: '))
p1=int(input('Digite a porta de entrada: '))
p2=int(input('Digite a porta de saida: '))
a=[]
for i in range(0,Q,1):
    l=int(input('Digite a quantidade de vida: '))
    a.append(l)
soma=0
for i in range(p1,p2+1,1):
    soma=soma+a[i]
print(soma)


