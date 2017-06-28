# -*- coding: utf-8 -*-

def crescente(lista):
    cont=0
    for i in range(1,len(lista),1):
        if lista[i]>lista[i-1]:
            cont=cont+1
    if cont==len(lista)-1:
        return True
    else:
        return False

def decrescente(lista):
    cont=0
    for i in range(1,len(lista),1):
        if lista[i]<lista[i-1]:
            cont=cont+1
    if cont==len(lista)-1:
        return True
    else:
        return False

def consecutivos(lista):
    for i in range(1,len(lista),1):
        if lista[i]==lista[i+1]:
            return True
        else:
            return False
        
n=int(input('digite o numero de termos:'))
lista1=[]
lista2=[]
lista3=[]
for i in range(0,n,1):
    num=int(input('digite o valor:'))
    lista1.append(num)
for i in range(0,n,1):
    num=int(input('digite o valor:'))
    lista2.append(num)
for i in range(0,n,1):
    num=int(input('digite o valor:'))
    lista3.append(num)

if crescente(lista1)==True:
    print('S')
else:
    print('N')
    
if decrescente(lista1)==True:
    print('S')
else:
    print('N')

if consecutivos(lista1)==True:
    print('S')
else:
    print('N')
    
if crescente(lista2)==True:
    print('S')
else:
    print('N')
    
if decrescente(lista2)==True:
    print('S')
else:
    print('N')

if consecutivos(lista2)==True:
    print('S')
else:
    print('N')
    
if crescente(lista3)==True:
    print('S')
else:
    print('N')
    
if decrescente(lista3)==True:
    print('S')
else:
    print('N')

if consecutivos(lista3)==True:
    print('S')
else:
    print('N')

        





#escreva o programa principal
