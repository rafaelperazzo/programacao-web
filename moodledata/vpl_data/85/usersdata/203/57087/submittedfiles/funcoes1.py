# -*- coding: utf-8 -*-

def crescente (lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]<lista[i+1]:
            
def decrescente (lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]>lista[i+1]:

def consecutivos (lista):
    for i in range(0,len(lista)-1,1):
        if lista[i]==lista[i+1]:
            return True
        else:
            return False

n=int(input('tamanho da lista: '))
A=[]
B=[]
C=[]
for i in range(1,n+1,1):
    a=int(input('elemento da lista A: '))
    A.append(a)
for i in range(1,n+1,1):
    b=int(input('elemento da lista B: '))
    B.append(b)
for i in range(1,n+1,1):
    c=int(input('elemento da lista C: '))
    C.append(c)

if crescente(A):
    print('S')
else:
    print('N')
if decrescente(A):
    print('S')
else:
    print('N')
if consecutivos(A):
    print('S')
else:
    print('N')
if crescente(B):
    print('S')
else:
    print('N')
if decrescente(B):
    print('S')
else:
    print('N')
if consecutivos(B):
    print('S')
else:
    print('N')
if crescente(C):
    print('S')
else:
    print('N')
if decrescente(C):
    print('S')
else:
    print('N')
if consecutivos(C):
    print('S')
else:
    print('N')