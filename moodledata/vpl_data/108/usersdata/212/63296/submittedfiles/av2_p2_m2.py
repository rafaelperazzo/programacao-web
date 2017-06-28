# -*- coding: utf-8 -*-
def somadasvidas (l,e,s):
    soma=0
    i=e
    while i<=s:
        soma=soma+l[i]
        i=i+1
    return (soma)
x=int(input('Digite a quantidade de elementos da lista:'))
lista=[]
i=0
while i<x:
    lista.append(input('Digite um elemento da lista:'))
    i=i+1
entrada=int(input('Digite o numero da porta de entrada:'))
saida=int(input('Digite o numero da porta de saida:'))
if entrada<saida:
    pe=entrada
    ps=saida
else:
    ps=entrada
    pe=saida
print(somadasvidas(lista,pe,ps))