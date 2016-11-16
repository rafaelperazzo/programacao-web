# -*- coding: utf-8 -*-
from __future__ import division

'''
1) PASSO 1: Criar a função média
'''

def media(a):
    soma = 0
    for i in range(0,len(a),1):
        soma = soma + a[i]
    
    return (soma/len(a))

'''
2) PASSO 2: 
'''

def somaNumerador(x,y):
    
    mediaX = media(x)
    mediaY = media(y)
    
    soma = 0
    for i in range(0,len(x),1):
        soma = soma + (x[i]-mediaX)*(y[i]-mediaY)
    
    return soma

#SOLUÇÃO 1
def somaDenominador(lista):
    soma = 0
    for i in range (0,len(lista),1):
        soma = soma + (lista[i]-media(lista))**2
    return soma

#SOLUÇÃO 2
def somaDenominador2(x,y): 
    resultado = somaNumerador(x,x)*somaNumerador(y,y)
    return resultado

#Utilizando a solução 2
def calcularP(x,y):    
    resultado = somaNumerador(x,y)/(somaDenominador2(x,y)**(0.5))
    return resultado
    
def calcularP2(x,y):
    resultado = somaNumerador(x,y)/((somaDenominador(x)*somaDenominador(y))**0.5)
    return resultado

n = input('Digite a quantidade de elementos: ')
x = []
y = []

for i in range(0,n,1):
    x.append(input('Digite um valor para x: '))

for i in range(0,n,1):
    y.append(input('Digite um valor para y: '))

print calcularP(x,y)





    
    
    