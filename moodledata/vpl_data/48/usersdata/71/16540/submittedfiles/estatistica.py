# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado
    
def desviop(lista):
    s=0
    for j in range(0,len(lista),1):
        p=(lista[j]-media(lista))**2
        s=s+p
        dpadrao=(s/(len(lista)-1))**(1/2)
        return dpadrao

n=input("Insira o Número de Elemento das Listas: ")
a=[]
b=[]

for k in range(0,n,1):
    a.append(input("Insira um Elemento da Lista a 
