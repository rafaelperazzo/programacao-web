# -*- coding: utf-8 -*-
import numpy as np
n=int(input('Digite o numero de linhas e colunas:'))
a=np.zeros((n,n))
for i in range (0, a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=float(input('Digite o valor:'))
def listadassomas (a):
    soma=0
    lista=[]
    for i in range (0,a.shape[0],1):
        soma=0
        for j in range (0,a.shape[1],1):
            soma=soma+a[i,j]
        lista.append(soma)
    for j in range (0,a.shape[1],1):
        soma=0
        for i in range (0,a.shape[0],1):
            soma=soma+a[i,j]
        lista.append(soma)
    soma=0
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            if i==j:
                soma=soma+a[i,j]
    lista.append(soma)
    cont=0
    cont2=a.shape[1]-1
    soma=0
    while cont2>=0:
        soma=soma+a[cont,cont2]
        cont=cont+1
        cont2=cont2-1
    lista.append(soma)
    for i in range (1,len(lista),1):
        if lista[i]!=lista[i-1]:
            return False
    return True
if listadassomas(a):
    print('S')
else:
    print('N')
