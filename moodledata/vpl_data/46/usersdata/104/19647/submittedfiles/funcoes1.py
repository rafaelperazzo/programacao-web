# -*- coding: utf-8 -*-
from __future__ import division
import math

def crescente (lista):
    for i in range(0,n,1):
        if i==(n-1):
            if lista[i-1]>lista[i]:
                return False
            else:
                return True
        
        elif lista[i]>lista[i+1]:
            break
            return False
        else:
            return True
def decrescente(lista):
    for i in range(0,n,1):
        if i==(n-1):
            if lista[i-1]<lista[i]:
                return False
            else:
                return True
        
        elif lista[i]<lista[i+1]:
            break
            return False
        else:
            return True
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
        return True
    else:
        return False
def teste(lista):
    
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
teste_1=teste(l1)
teste_2=teste(l2)
teste_3=teste(l3)

print teste_1
print teste_2
print teste_3


