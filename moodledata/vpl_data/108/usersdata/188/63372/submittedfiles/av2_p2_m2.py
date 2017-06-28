# -*- coding: utf-8 -*-
salas=int(input('digite a quantidade de salas:'))
lista=[]
for i in range(0,salas,1):
    v=int(input('digite o numero de vidas:'))
    lista.append(v)
pe=int(input('digite a porta de entrada:'))
ps=int(input('digite a porta de saída:'))
soma=0
for i in range(pe,ps+1,1):
    soma=soma+lista[i]
print(soma)

