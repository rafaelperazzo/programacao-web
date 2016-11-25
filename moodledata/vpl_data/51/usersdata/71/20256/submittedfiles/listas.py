# -*- coding: utf-8 -*-
from __future__ import division

n=input("Insira o Número de Termos: ")
a=[]
for i in range(0,n,1):
    a.append(input("Insira um Elemento: "))
    
def valor_absoluto(x):
    if x<0:
        return -x
    else:
        return x
def degraus(lista):
    degraus=[]
    for i in range(0,len(lista)-1,1):
        degraus.append(valor_absoluto(lista[i]-lista[i+1]))
    return degraus
def maior(lista):
    maior=0
    for i in range(0,len(lista),1):
        if lista[i]>maior:
            maior=lista[i]
    return maior

print maior(degraus(a))