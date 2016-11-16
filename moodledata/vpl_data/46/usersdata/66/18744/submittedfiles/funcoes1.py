# -*- coding: utf-8 -*-
from __future__ import division

def crescente (lista):
    cont=0
    for i in range(0,lken(lista)-1,1):
        if 1==0:
            if lista [i]<lista [1]:
                cont=cont +1
        elif i==(len(lista)-1):
            if lista[len(lista)-1]>lista[len(lista)-2]:
            cont=cont+1
        else:
            if lista[i]>lista[i-1] and lista[i]<lista[i+1]:
                cont=cont+1
        if cont==(len(lista)-1):
            return true
        else:
            return false
def decrescente (lista):
    cont=0
    for i in range (0 ,len(lista)-1,1):
        if i==0
            if lista[i]>lista[1]:
                cont=cont+1
        elif i==(len(lista)-1):
            if lista[len(lista)-1]<lista[len(lista)-2]:
                cont=cont+1
        else:
            if lista[i]==lista[i-1] or lista[i]==lista[i+1]:
                conf-cont+1
    if cont>0
        return True
    else:
        return False
n=int(input("digite a quantidade de termos"))
a=[]
b=[]
c=[]

for i in range (0,n,1):
    a. append(input("Digite os valores da lista a:"))
for i in range (0,n,1):
    b.append(input("Digite os valores da lista b:"))
for i in range (0,n,1):
    c.append(input("digite os valores da lista c"))
if crescent(a):
    print ("S")
else:
    print ("N")
    
if descrecente(a):
    print ("S")
else:    
    print ("N")
if consecutivos(a):
    print ("S")
else:
    print ("N")
    
if crescente (b):
    print ("S")
else
    print ("N")
    
if decrescente(b):
   print("S")
else
   print("N")
if consecutivos(b):
    print("S")
else
    print("N")


if crescente (c):
    print ("S")
else
    print ("N")
    
if decrescente(c):
   print("S")
else
   print("N")
if consecutivos(c):
    print("S")
else
    print("N")
    





