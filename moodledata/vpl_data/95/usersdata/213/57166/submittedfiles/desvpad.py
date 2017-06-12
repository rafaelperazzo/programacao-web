# -*- coding: utf-8 -*-
import math

n=int(input('Informe a quantidade de elementos da lista: '))
lista=[]
for i in range(0,n,1):
    elemento=int(input('Informe os elementos da lista: '))
    lista.append(elemento)

soma=0
for i in range(0, len(lista),1):
    soma=soma+lista[i]
media=soma/len(lista)

desvPad=0
for i in range(0, len(lista),1):
    desvPad=desvPad+((lista[i]-media)**2)
desvioPadrao=(desvPad/(len(lista-1))**0.5

print('%.2f' %lista[0])
print('%.2f' %lista[-1])
print('%.2f' %media)
print('%.2f' %desvioPadrao)
    
