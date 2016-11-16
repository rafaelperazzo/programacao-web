# -*- coding: utf-8 -*-
from __future__ import division

def crescente(lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]>=lista[i+1]:
            cont=cont+1
    if cont==0:
        return True
    else:
        return False
    
def dcrescente(lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]<=lista[i+1]:
            cont=cont+1
    if cont==0:
        return True
    else:
        return False

def igual(lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]==lista[i+1]:
            cont=cont+1
    if cont!=0:
        return True
    else:
        return False

n=input()
a=[]
b=[]
c=[]
for j in range(0,n,1):
    a.append(input())
for k in range(0,n,1):
    b.append(input())
for l in range(0,n,1):
    c.append(input())

if crescente(a):
    print "S"
else:
    print "N"
    


