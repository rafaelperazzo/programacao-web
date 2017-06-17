# -*- coding: utf-8 -*-

def crescente (lista):
    contador=0
    for i in range(1,len(lista),1):
        if lista[i]>lista[i-1]:
            contador=contador+1
    if contador!=0:
        return (True)
    else:
        return (False)

def decrescente (lista):
    contador=0
    for i in range(1,len(lista),1):
        if lista[i]<lista[i-1]:
            contador=contador+1
    if contador!=0:
        return (True)
    else:
        return (False)

def iguais (lista):
    contador=0
    for i in range(1,len(lista),1):
        if lista[i]==lista[i-1] :
            contador=contador+1
    if contador!=0:
        return (True)
    else:
        return (False)
#escreva o programa principal
n=int(input('Informe a quantidade de digitos das listas: '))
lista1=[]
lista2=[]
lista3=[]
for i in range(0,n,1):
    elemento=int(input('Informe os elementos da lista 1: '))
    lista1.append(elemento)
    
for i in range(0,n,1):
    elemento=int(input('Informe os elementos da lista 2: '))
    lista2.append(elemento)
    
for i in range(0,n,1):
    elemento=int(input('Informe os elementos da lista 3: '))
    lista3.append(elemento)

if crescente (lista1):
    print('S')
else:
    print('N')

if decrescente (lista1):
    print('S')
else:
    print('N')

if iguais (lista1):
    print('S')
else:
    print('N')

if crescente (lista2):
    print('S')
else:
    print('N')

if decrescente (lista2):
    print('S')
else:
    print('N')

if iguais (lista2):
    print('S')
else:
    print('N')
    
if crescente (lista3):
    print('S')
else:
    print('N')

if decrescente (lista3):
    print('S')
else:
    print('N')

if iguais (lista3):
    print('S')
else:
    print('N')