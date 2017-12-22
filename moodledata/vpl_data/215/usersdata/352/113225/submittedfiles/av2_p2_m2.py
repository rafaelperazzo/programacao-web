# -*- coding: utf-8 -*-


n=int(input('Numero de salas: '))
a=[]
for i in range(0,n,1):
    a.append(int(input('Quantidade de vidas da sala: ')))
e=int(input('Porta de entrada: '))
s=int(input('Porta de saída: '))
vidas=0
for i in range(e,s+1,1):
    vidas=vidas+a[i]
print(vidas)