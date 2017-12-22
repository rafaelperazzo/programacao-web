# -*- coding: utf-8 -*-


def media(lista):
    media=sum(lista)/len(lista)
    return media
    
def desvio_padrao(lista):
    somatorio=0
    for i in range(0,len(lista),1):
        somatorio= ((media(lista)-lista[i])**2)
    desvio=(somatorio/(n-1))**0.5
    return desvio

m=int(input("Digite o número de listas: "))
n=int(input("Digite o número de elementos de cada lista: "))

for i in range