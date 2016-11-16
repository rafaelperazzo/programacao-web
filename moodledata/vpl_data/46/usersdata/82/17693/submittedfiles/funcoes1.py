# -*- coding: utf-8 -*-
from __future__ import division

def crescente (lista):
    cont=0
    for i inrange (0,len(lista,1)):
        if i==0:
            if lista[i]<lista[i+1]<lista[i+2]
            cont=conta+1
        elif i==(len(lista)-1):
            if lista[len(lista)-1]:
                if lista[len(lista)-1]>lista[len(lista)-2]>lista[len(lista)-3]:
                    con=cont+1
        else:
            if lista[i]==lista[i+1] or lista[i+1]==lista[i+2]:
                cont=cont+1

    if cont==1:
        return True
    else:
        return False

a=[]
b=[]
c=[]

n= input ('Digite o valor de n:')
for i in range (0,n,1):
    a.append (input('Digite o valor de a:'))
for i in range (0,n,1):
    b.append (input('Digite o valor de b:'))
for i in range (0,n,1):
    c.append (input('digite o valor de c:'))

if crescente(a):
    print ('S')






#escreva o programa principal
