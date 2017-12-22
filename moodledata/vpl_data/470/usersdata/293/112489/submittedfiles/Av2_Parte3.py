# -*- coding: utf-8 -*-
def media(lista):
    media= sum(lista)/len(lista)
    return media

def desvio(lista):
    somatorio=0
    for i in range(0,len(lista),1):
        somatorio= somatorio + ((lista[i]-media(lista))**2)
    desvio= ((somatorio/(len(lista)-1))**0.5)
    return desvio

m=int(input("Digite o número de listas: "))
n=int(input("Digite o número de elementos de cada lista: "))

grupos=[]


for i in range(0,m,1):
    grupos_linha=[]
    for j in range(0,n,1):
        grupos_linha(int(input("Digite o valor do elemento (%d,%d): "%(i+1,j+1))))
    grupos.append(grupos_linha)


for k in range(0,m,1):
    print(media(grupos[k]))
    print(desvio(grupos[k]))
    k=k+1
