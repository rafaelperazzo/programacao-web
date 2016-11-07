# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

def desviop(lista) :
    soma = 0
    for i in range (0,len(lista),1):
        soma=soma+((lista[i]-media)**2)
    resultado=(soma/(n-1))**0.5
    return resultado

la=[]
lb=[]
a=input('Digite o tamanho da lista:  ')

for i in range (0,a,1) :
    la.append(input('Digite o valor do elemento: ')

b=input('Digite o tamnho da segunda lista: ')

for i in range (0,b,1) :
    lb.append(input('Digite o valor do elemento: ')

mediaLa=media(la)
desviopLa=desviop(la)
mediaLb=media(lb)
desviopLb=desviop(lb)

print mediaLa
print desviopLa
print mediaLb
print desviopLb