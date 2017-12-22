# -*- coding: utf-8 -*-
import math

#comece abaixo
#função desvio padrão:
def desvio(a,media):
    somatoria=0
    for i in range(0,len(a)-1,1):
        somatorio=somatorio+(a[i]-media)**2
    s=((1/(len(a)-1))*somatoria)**0.5
    return(s)

#PROGRAMA:
n=int(input('Quantidade de valores: '))
lista=[]
soma=0
for i in range(0,n,1):
    elem=int(input('Digite o valor do elemento: '))
    lista.append(elem)
    soma=soma+elem
media=soma/n
print('%.2f' %lista[0])
print('%.2f' %lista[n-1])
print('%.2f' %media)
print(desvio(lista,media))