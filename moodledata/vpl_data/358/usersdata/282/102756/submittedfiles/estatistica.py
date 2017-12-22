# -*- coding: utf-8 -*-


def media(lista):
    media=sim(lista)/len(lista)
    return media
    
def desvio_padrao(lista):
    somatorio=0
    for i in range(0,len(lista),1):
        somatorio=((media(lista)-lista[i])**2) + somatorio
    desvio=(somatorio/(n-1))**0.5
    return desvio
    
m= int(input('Digite o numero de listas: '))
n= int(input('Digite o numero de elementos de cada lista: '))
matriz=[]
for i in range(0,m,1):
    matriz_linha=[]
    for j in range(0,n,1):
        matriz_linha.append(int(input('Digite o elemento (%d,%d): '%(i+j,j+i))))
    matriz.append(matriz_linha)
    
for i in range(0,m,1):
    print(media(matriz[i]))
    print('%.2f'%(desvio_padrao(matriz[i])))