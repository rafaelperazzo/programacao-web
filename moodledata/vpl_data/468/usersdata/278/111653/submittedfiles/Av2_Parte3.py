# -*- coding: utf-8 -*-
m=int(input('Digite a quantidade de listas: '))
n=int(input('Digite a quantidade de elementos de cada lista: '))
matriz=[]
for i in range (0,m,1):
    lista=[]
    for j in range (0,n,1):
        lista.append(int(input('Digite o elemento%.d da lista%.d: ' %(j+1,i+1))))
    matriz.append(lista)
soma_media=0
for i in range (0,m,1):
    soma=0
    for j in range (0,n,1):
        soma+=matriz[i][j]
    print(soma)
    media=soma/(n)
    print(media)
    for j in range (0,n-1,1):
        soma_media+=(matriz[i][j]-media)**2
    s=((1/(n-1))*soma_media)**(1/2)
    print('%.2f' %(s))