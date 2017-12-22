# -*- coding: utf-8 -*-
n= int(input('Digite a quantidade de valores da lista:'))
a=[]
for i in range(0,n,1):
    int(input('Digite o valor de cada termos da lista:'))
    a=[]
    
print (len(a))
def media (lista):
    soma=0
    for i in range (0,len(lista),1):
        soma= soma+lista[i]
    resultado= soma/len(lista)
    return (resultado)