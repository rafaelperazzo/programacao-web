# -*- coding: utf-8 -*-
m=int(input('digite o numero de lista que deseja: '))
n=int(input('digite o numero de elementos que deseja para cada lista: '))
matriz=[]
for i in range(0,m,1):
    lista=[]
    for j in range(0,n,1):
        lista.append(int(input('digite o elemento da lista%d e posicao %d: '%((i+1),(j+1)))))
    matriz.append(lista)
def median(lista,n):
    med=0
    for k in range(0,n,1):
        med=med+lista[k]
    media=med/n
    return media
def desvpad(lista,n):
    med=0
    somatorio=0
    for k in range(0,n,1):
        med=med+lista[k]
    media=med/n
    for l in range(0,n,1):
        somatorio=somatorio+((lista[l]-media)**2)
    s=((1/(n-1))*somatorio)**(0.5)
    return s
for i in range(0,n,1):
    print(median(matriz[i],n))
    print(desvpad(matriz[i],n))
    