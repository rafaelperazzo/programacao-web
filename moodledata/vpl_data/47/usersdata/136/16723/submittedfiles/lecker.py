# -*- coding: utf-8 -*-
from __future__ import division

def lecker (lista):
    cont=0
    for i in range (1,n-1,1):
        if lista[i]>lista[i-1] and lista[i]>lista[i+1]:
            cont = cont+1
    if lista[0]>lista[1]:
        cont = cont+1
    
    if cont == 1:
        return True
    else:
        return False
        
a=[]
b=[]
n = input("Digite o número de elementos:")

for i in range (0,n,1):
    a.append(input("Digite um elemento A:"))
for i in range (0,n,1):
    b.append(input("Digite um elemento B:"))

if lecker(a):
    print "S"
else:
    print "N"
if lecker(b):
    print "S"
else:
    print "N"