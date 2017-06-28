# -*- coding: utf-8 -*-
import numpy as np
x=int(input('Digite o numero de linhas:'))
b=np.zeros((x,x))
for i in range (0,b.shape[0],1):
    for j in range(0,b.shape[1],1):
        b[i,j]=int(input('Digite um numero:'))
def somac(a):
    lista=[]
    for j in range (0,a.shape[1],1):
        soma=0
        for i in range (0,a.shape[0],1):
            soma=soma+a[i,j]
        lista.append(soma)
    return (lista)
somacoluna=somac(b)
def somal(a):
    soma=0
    lista=[]
    for i in range (0,a.shape[0],1):
        soma=0
        for j in range (0,a.shape[1],1):
            soma=soma+a[i,j]
        lista.append(soma)
    return (lista)
somalinha=somal(b)
def dif (lista):
    for i in range (0,len(lista),1):
        contador=0
        for j in range (0,len(lista),1):
            if lista[i]==lista[j]:
                contador=contador+1
        if contador==1:
            return(i)
            
def igualdade (lista):
    for i in range (0,len(lista),1):
        contador=0
        for j in range (0,len(lista),1):
            if lista[i]==lista[j]:
                contador=contador+1
        if contador>1:
            return(j)

li=dif(somalinha)
co=dif(somacoluna)
r=(b[li,co]-(dif(somalinha)-igualdade(somalinha)))
print('%d'%r)
print('%d'%b[li,co])
