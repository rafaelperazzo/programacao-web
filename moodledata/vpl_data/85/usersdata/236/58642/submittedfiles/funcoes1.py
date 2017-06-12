# -*- coding: utf-8 -*-

def crescente (lista):
    cont=0
    for i in range (1,len(lista),1):
        if lista[i]>lista[i-1]:
            cont=cont+1
    if cont==len(lista)-1:
        return True
    else:
        return False

def decrescente (lista):
    for i in range (1,len(lista),1):
        if lista[i]<lista[i-1]:
            cont=cont+1
    if cont==len(lista)-1:
        return True
    else:
        return False








#escreva o programa principal
N = float(input('n:'))

A=[]
B=[]
C=[]

for i in range (1,n+1,1):
    numero = float(input('num:'))
    A.append (numero)
for i in range (1,n+1,1):
    numero = float(input('num:'))
    B.append (numero)
for i in range (1,n+1,1):
    numero = float(input('num:'))
    C.append (numero)
