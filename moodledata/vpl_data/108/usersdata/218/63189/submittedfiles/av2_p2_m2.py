# -*- coding: utf-8 -*-
n=int(input('digite o numero de salas da lista:'))
a=[]
for i in range (0,n,1):
    valor=int(input('digite a variação de vida da sala:'))
    a.append(valor)
e=int(input('digite a porta de entrada:'))
s==int(input('digite a porta de saida:'))
nv=0
for i in range (e,(s+1),1):
    nv=nv+a[i]
print(nv)