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
lista=[]
for i in range(0,m,1):
    lista_linha=[]
    for j in range(0,n,1):
        lista_linha(int(input("Digite o valor do %dº elemento da %dª lista: "%(j+1,i+1))))
    lista.append(lista_linha)

for k in range(0,m,1):
    print(media(lista[k]))
    print(desvio(lista[k]))
    k=k+1
