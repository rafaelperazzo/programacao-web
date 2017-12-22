# -*- coding: utf-8 -*-
m=int(input('digite o numero de lista que deseja: '))
n=int(input('digite o numero de elementos que deseja para cada lista: '))
matriz=[]
for i in range(0,m,1):
    lista=[]
    for j in range(0,n,1):
        lista.append(int(input('digite o elemento da lista%d e posicao %d: '%((i+1),(j+1)))))
    matriz.append(lista)
def desvpad(lista,n):
    media=0
    for k in range(0,m,1):
        media=media+lista[i]
    for l in range(0,m,1):
        somatorio=somatorio+((lista[i]-media)**2)
    s=((1/(n-1))*somatorio)**(0.5)
    
    return media
    return s
for i in range(0,n,1):
    print('%.2f'desvpad(matriz[i],n))
    