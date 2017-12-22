# -*- coding: utf-8 -*-
m= int(input('Digite a quantidade de listas: '))
n= int(input('Digite a quantidade de elementos das listas: ')) 
for i in range (0,m,1):
    lista=[]
    for i in range (0,n,1):
        lista.append(int(input('Digite o elemento %d da lista: ' %(i+1))))
#MEDIA
    soma=0
    for i in range (0,n,1):
        soma+=lista[i]
    media=soma/n
    print('%.2f' %(media))
#DESVIO PADRAO
    som=0
    for i in range (0,n,1):
        som+=(lista[i]-media)**2
    s=(som/(n-1))**0.5
    print('%.2f' %(s))
