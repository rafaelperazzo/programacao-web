# -*- coding: utf-8 -*-
from __future__ import division

def crescente (lista):
   cont=0
   for i in range (0,len(lista),1):
       if lista[i]<lista[i+1]:
           cont=cont+1
           return True
       else:
           return False

def decrescente (lista):
    cont=0
    for i in range (0,len(lista),1):
       if lista[i]>lista[i+1]:
           cont=cont+1
           return True
       else:
           return False
            
def consecutivos (lista):
    cont=0
    for i in range (0,len(lista)-1,1):
       if lista[i]==lista[i+1]:
           cont=cont+1
           return True
       else:
           return False 
            
a=[]
b=[]
c=[]
n=input("digite a quantidade de elementos:")
for i in range(0,n,1):
    a.append(input("digite elemento:"))
for i in range(0,n,1):
    b.append(input("digite elemento:"))
for i in range(0,n,1):
    c.append(input("digite elemento:"))

if crescente (a):
    print("S")
else:
    print("N")
if decrescente (a):
    print("S")
else:
    print("N")
if consecutivos (a):
    print("S")
else:
    print("N")
if crescente (b):
    print("S")
else:
    print("N")
if decrescente (b):
    print("S")
else:
    print("N")
if consecutivos (b):
    print("S")
else:
    print("N")
if crescente (c):
    print("S")
else:
    print("N")
if decrescente (c):
    print("S")
else:
    print("N")
if consecutivos (c):
    print("S")
else:
    print("N")