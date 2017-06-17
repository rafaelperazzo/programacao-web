# -*- coding: utf-8 -*-

def crescente (lista):
    cont=0
    for i in range(0,len(lista),1):
        if lista[i]>lista[i-1]:
            cont=cont+1
    if cont==len(lista)-1:
        return True
    else:
        return False

def decrescente(lista):
    cont=0
    for i in range(0,len(lista),1):
        if lista[i]<lista[i-1]:
            cont=cont+1
    if cont==len(lista)-1:
        return True
    else:
        return False

def consecutivo(lista):
    cont=0
    for i in range(0,len(lista),1):
        if i==0:
            if lista[i]==lista[i+1]:
                cont=cont+1
        elif i==len(lista)-1:
            if lista[i]==lista[i-1]:
                cont=cont+1
        else:
            if lista[i]==lista[i+1] or lista[i]==lista[i-1]:
                cont=cont+1
    if cont!=0:
        return True
    else:
        return False

n=int(input('digite n:'))
lista1=[]
lista2=[]
lista3=[]
for i in range(1,n+1,1):
    a=float(input('digite a:'))
    lista1.append(a)
for i in range(1,n+1,1):
    b=float(input('digite b:'))
    lista2.append(b)
for i in range(1,n+1,1):
    c=float(input('digite c:'))
    lista3.append(c)
if crescente(lista1):
    print('S')
else:
    print('N')
if decrescente(lista1):
    print('S')
else:
    print('N')
if consecutivo(lista1):
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
if consecutivo(lista2):
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
if consecutivo(lista3):
    print('S')
else:
    print('N')
        




