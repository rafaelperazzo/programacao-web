# -*- coding: utf-8 -*-
n=int(input('Informe a quantidade de elementos:'))
lista1=[]
lista2=[]
lista3=[]

for i in range(1,n+1,1):
    numero=float(input('Digite um número:'))
    lista1.append(numero)
for i in range(1,n+1,1):
    numero=float(input('Digite um número:'))
    lista2.append(numero)  
for i in range(1,n+1,1):
    numero=float(input('Digite um número:'))
    lista3.append(numero)   
    
def crescente (lista):
    cont=0
    for i in range(1,len(lista),1):
        if lista[i] > lista[i-1]:
            cont=cont+1
        if cont==(len(lista)-1):
            return True
        else:
            return False

def decrescente (lista):
    cont=0
    for i in range(1,len(lista),1):
        if lista[i] < lista [i-1]:
            cont=cont+1
        if cont==len(lista)-1:
            return True
        else:
            return False
            
def consecutivos (lista):
    cont=0
    for i in range(1,len(lista),1):
        if lista[i] == lista[i-1]:
            cont=cont+1
        if cont!=0:
            return  True
        else:
            retunr False
#escreva o programa principal
if crescente(lista1):
    print('S')
else:
    print('N')
if decrescente(lista1):
    print('S')
else:
    print('N')
if consecutivos(lista1):
    print('S')
else:
    print('N')
if crescente(lista2):
    print('S')
else:
    print('N')
if decrescente(lista2):
    print('S')
else:
    print('N')
if consecutivos(lista2):
    print('S')
else:
    print('N')
if crescente(lista3):
    print('S')
else:
    print('N')
if decrescente(lista3):
    print('S')
else:
    print('N')
if consecutivos(lista3):
    print('S')
else:
    print('N')    
    