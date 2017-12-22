# -*- coding: utf-8 -*-


n=int(input('Quantidade de salas: '))
a=[]
for i in range(0,n,1):
    a.append(int(input('Digite a quantidade de vidas da sala %d: ' %i)))
e=int(input('Digite a porta de entrada: '))
s=int(input('Digite a porta de saída: '))
vidas=0
for i in range(e,s+1,1):
    vidas=vidas+a[i]
print(vidas)