# -*- coding: utf-8 -*-
n=int(input('digite n:'))
lista1=[]
for i  in range(0,n,1):
    a=float(input('digite a:'))
    lista1.append(a)
lista2=[]
for i  in range(0,n,1):
    b=float(input('digite b:'))
    lista2.append(b)
lista3=[]
for i  in range(0,n,1):
    c=float(input('digite a:'))
    lista3.append(c)
def crescente (lista):
    cont=0
    for i in range(1,len(lista),1):
        if lista[i]>lista[i-1]:
            cont=cont+1
if cont==len(lista)-1:
    return True
else:
    return False
def decrescente (lista):
    cont=0
    for i in range(1,len(lista),1):
        if lista[i]<lista[i-1]:
            cont=cont+1
if cont==len(lista)-1:
    return False
else:
    return True
def consecutivos (lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista==lista[i+1]:
            cont=cont+1
if cont==0:
    return False
else:
    return True