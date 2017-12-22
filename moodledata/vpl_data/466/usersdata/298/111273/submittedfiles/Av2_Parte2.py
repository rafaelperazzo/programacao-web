# -*- coding: utf-8 -*-
def crescente(lista):
    h=len(lista)
    cont=0
    for i in range (0, h-1, 1):
        if lista[i]<lista[i+1]:
            cont+=0
        if not lista[i]<lista[i+1}:
            cont+=1
            break
    if cont==0:
        cresc=True
    if not cont==0:
        cresc=False
    return cresc

def decrescente(lista):
    h=len(lista)
    cont=0
    for i in range (0, h-1, 1):
        if lista[i]>lista[i+1]:
            cont+=0
        if not lista[i]>lista[i+1]:
            cont+=1
            break
    if cont==0:
        decresc=True
    if not cont==0:
        decresc=False
    return decresc

def consecutivos(lista):
    h=len(lista):
    cont=0
    for i in range (0, h-1, 1):
        if lista[i]==lista[i+1]:
            cont+=1
            break
        if not lista[i]==lista[i+1]:
            cont+=0
    if cont==0:
        consec=False
    if not cont==0:
        consec=True
    return consec

n=int(input('Digite o numero n de elementos: '))

l1=[]
l2=[]
l3=[]
for i in range (0, n, 1):
    l1.append(int(input('Digite um elemento para a lista 1: ')))
for i in range (0, n, 1):
    l2.append(int(input('Digite um elemento para a lista 2: ')))
for i in range (0, n, 1):
    l3.append(int(input('Digite um elemento para a lista 3: ')))

if 