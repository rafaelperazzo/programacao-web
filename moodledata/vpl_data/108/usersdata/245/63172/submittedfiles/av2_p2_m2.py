# -*- coding: utf-8 -*-
n=int(input('Digite o Número de Salas:'))
lista=[]
for i in range(1,n+1,1):
    v=int(input('Digite o número de vidas da sala:'))
    lista.append(v)
pi=int(input('Digite a porta de entrada:'))
ps=int(input('Digite a porta de saida:'))
for i in range(pi,ps+1,1):
    print(lista[i])
