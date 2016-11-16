# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO

#DEFININDO A FUNÇÃO
def media(x):
    soma=0
    for i in range(0,len(x),1):
        soma=soma+x[i]
    media=soma/len(x)
    return media
def soma(x,y):
    soma=0
    for i in range(0,len(x),1):
        soma=soma+(x[i]-media(x))*(y[i]-media(y))
    return soma
def soma2(x):
    soma=0
    for i in range(0,len(x),1):
        soma=soma+(x[i]-media(x))**2
    return soma
def person(x,y):
    p=(soma(x,y))/((soma2(x)*soma2(y))**0.5)
    
    return p
        
#ENTRADA
n=input('Digite a quantidade de termos das Listas: ')
lista=[]
prova=[]
for i in range(0,n,1):
    lista.append(input('Digite o valor de uma das notas da lista: '))
    
for i in range(0,n,1):
    prova.append(input('Digite o valor de uma das notas da prova: '))
    
if person(lista,prova)>=0.9:
    print('Muito Forte')
if 0.7<=person(lista,prova)<0.9:
    print('Forte')
if 0.5<=person(lista,prova)<0.7:
    print('Moderada')
if 0.3<=person(lista,prova)<0.5:
    print('Fraca')
if 0<=person(lista,prova)<0.3:
    print('Desprezível')
    
print media(lista)
print soma(lista,prova)
print soma2(lista)
print person(lista,prova)

print media(prova)

print soma2(prova)


