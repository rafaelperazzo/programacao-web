# -*- coding: utf-8 -*-
from __future__ import division

def lecker(x):
    cont=0
    for i in range(0,len(x),1):
        if i==0:
            if x[i]>x[i+1]:
                cont=cont+1
        elif i==(len(x)-1):
            if x[i]>x[i-1]:
                cont=cont+1
        else:
            if x[i]>x[i+1] and x[i]>x[i-1]:
                cont=cont+1
    if cont==1:
        return True
    else:
        return False

a=[]
b=[]
n=input("Insira o Número de Elemento das Listas: ")
for i in range(0,n,1):
    a.append(input("Insira Um Elemento da Lista A: ")
for j in range(0,n,1):
    b.append(input("Insira Um Elemento da Lista B: ")
    
if lecker(a):
    print "S"
else:
    print "N"
    
if lecker(b):
    print "S"
else:
    print "N"
