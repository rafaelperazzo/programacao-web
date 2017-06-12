# -*- coding: utf-8 -*-
a=int(input('Digite o numero de elementos da primeira lista:'))
b=int(input('Digite o nummero de elementos da segunda lista:'))
listaA=[]
listaB=[]
contador=0
for i in range (0,a,1):
    valor=int(input('Digite um elemento da primeira lista:'))
    listaA.append(valor)
for i in range (0,b,1):
    valorb=int(input('Digite um elemento da segunda lista:'))
    listaB.append(valorb)
for i in range(0,len(listaA),1):
    for j in range (0,len(listaB),1):
        if listaA[i]==listaB[j]:
            contador=contador+1
print(contador)