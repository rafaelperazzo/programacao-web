# -*- coding: utf-8 -*-
n=int(input('Digite o numero de elementos da lista:'))
lista=[]

for i in range(0,len(lista),1):
    valor=int(input('Digite o valor de um numero da lista:'))
    lista.append(valor)
pe=int(input('Digite o indice da porta de entrada:'))
ps=int(input('Digite o indice da porta de saida:'))
if pe<ps:
    entrada=pe
    saida=ps
else:
    entrada=ps
    saida=pe
soma=0
for i in range (entrada,saida+1,1):
    soma=soma+lista[i]
print(soma)