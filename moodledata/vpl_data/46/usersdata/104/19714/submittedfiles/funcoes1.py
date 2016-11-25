# -*- coding: utf-8 -*-
from __future__ import division
import math

def crescente (lista):
    for i in range(0,n,1):
        if i==(n-1):
            if lista[i-1]>lista[i]:
                return ('N')
            else:
                return ('S')
        
        elif lista[i]>lista[i+1]:
            return ('N')
            break
        else:
            return ('S')
def decrescente(lista):
    for i in range(0,n,1):
        if i==(n-1):
            if lista[i-1]<lista[i]:
                return ('N')
            else:
                return ('S')
        
        elif lista[i]<lista[i+1]:
            break
            return ('N')
        else:
            return ('S')
def consec(lista):
    cont=0
    for i in range(0,n,1):
        if i==(n-1):
            if lista[i-1]==lista[i]:
                cont=cont+1
            break
        elif lista[i]==lista[i+1]:
            cont=cont+1
    if cont>0:
        return ('S')
    else:
        return ('N')
    
n=input('Digite o valor de n:')
l1=[]
l2=[]
l3=[]
for i in range(0,n,1):
    l1.append(input('Digite um valor para lista 1:'))
for i in range(0,n,1):
    l2.append(input('Digite um valor pra lista 2:'))
for i in range(0,n,1):
    l3.append(input('Digite um valor pra lista 3:'))

print crescente(l1)
print decrescente(l1)
print consec(l1)
print crescente(l2)
print decrescente(l2)
print consec(l2)
print crescente(l3)
print decrescente(l3)
print consec(l3)


