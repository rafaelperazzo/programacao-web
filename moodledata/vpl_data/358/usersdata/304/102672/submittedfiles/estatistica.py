# -*- coding: utf-8 -*-


def media(lista):
    media=sum(lista)/len(lista)
    return media
    
def d_p(lista):
    soma=0
    for i in range(0,len(lista),1):
        soma=((media(lista)-lista[i])**2)+soma
    desvio=(soma/(n-1))**0.5
    return desvio

matriz = []
m = int(input('Digite a quantidade de linhas: '))
n = int(input('Digite a quantidade de colunas: '))
for i in range (0,m,1):
    linha = []
    for j in range (0,n,1):
        linha.append(int(input('Digite o elemento: ')))
    matriz.append(linha)
    
for i in range(0,m,1):
    print(media(matriz[i]))
    print('%.2f'%(d_p(matriz[i])))
