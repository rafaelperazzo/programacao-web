# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO
def med(lista):
    soma=0
    for i in range (0, len(lista),1):
        soma= soma + lista[i]
    media= soma/ len(lista)
    return media

def soma1(lista1, lista2):
    soma=0
    for i in range (0,len(lista1),1):
        soma= soma +((lista1[i]-med(lista1))*(lista2[i]-med(lista2)))
    return soma

def soma2(lista):
    soma=0
    for i in range (0,len(lista),1):
        soma =soma+ ((lista[i]-med(lista))**2)
    return soma

n= input('Insira a quantidade de termos:')
x=[]
y=[]
for i in range (0,n,1):
    x.append(input('Insira os valores de x:'))
for i in range (0,n,1):
    y.append(input('Insira os valores de y:'))
    
p= soma1(x,y)/((soma2(x) * soma2(y))**(1/2))

print (p)