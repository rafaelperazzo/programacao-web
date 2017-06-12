# -*- coding: utf-8 -*-
from __future__ import division
def lecker (lista):
    c=0
    for i in range (0,len(lista),1):
        if lista[i-1]<lista[i]>lista[i+1]:
            c=c+1
    if c==1:
        return True
    else:
        return False
        
N=int(input("Digite a quantidade de elementos: "))
a=[]
b=[]
for i in range(0,N,1):
    a.append(int(input("Digite o termo: ")))
for i in range(0,N,1):
    b.append(int(input("Digite o termo: ")))
if lecker(a):
    print("S")
else:
    print("N")
    
if lecker(b):
    print("S")
else:
    print("N")
