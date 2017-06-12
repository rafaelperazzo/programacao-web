# -*- coding: utf-8 -*-

def crescente(lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]<lista[i+1]:
            cont=cont+1
    if cont==(len(lista)-1):
        return True
    else:
        return False
def decrescente(lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]>lista[i+1]:
            cont=cont+1
    if cont==(len(lista)-1):
        return True
    else:
        return False
def iguais(lista):
        for i in range(0,len(lista)-1,1):
            if lista[i]==lista[i+1]:
                return True
    else:
        return False
n=int(input('Digite a Quantidade de Elementos da Lista:'))
l1=[]
for i in range(1,n+1,1):
    v1=int(input('Digite os Elementos da L1:'))
    l1.append(v)
    
l2=[]
for i in range(1,n+1,1):
    v2=int(input('Digite os Elementos da L2:'))
    l2.append(v)
    
l3=[]
for i in range(1,n+1,1):
    v1=int(input('Digite os Elementos da L3:'))
    l3.append(v)
    
if crescente(l1):
    print('S')
else: 
    print('N')
if decrescente(l1):
    print('S')
else:
    print('N')
if iguais(l1):
    print('S')
else:
    print('N')
    
if crescente(l2):
    print('S')
else: 
    print('N')
if decrescente(l2):
    print('S')
else:
    print('N')
if iguais(l2):
    print('S')
else:
    print('N')

if crescente(l3):
    print('S')
else: 
    print('N')
if decrescente(l3):
    print('S')
else:
    print('N')
if iguais(l3):
    print('S')
else:
    print('N')
