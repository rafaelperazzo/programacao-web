# -*- coding: utf-8 -*-
from __future__ import division

def crescente (a):
    cont=0
    for i in range (0,len(a)-1,1):
        if a[i]>a[i+1]:
            cont=cont+1
    if cont==0:
        return true
    else:
        return false
        
def decresc(a):
    cont=0
    for i in range (0,len(a)-1,1):
        if a[i]<a[i+1]:
            cont=cont + 1
    if cont==0:
        return true
    else:
        return false
    
def elecon(a):
    cont=0
    for i in range (0,len(a)-1,1):
        if a[i]==a[i-1] or a[i]==a[i+1]:
            cont=cont + 1
    if cont!=0:
        return true
    else:
        return false
a=[]
b=[]
c=[]
n=int(input("digite um valor:"))

for i in range (0,n,1): 
    a.append (input ("digite um número:"))
for i in range (0,n,1):
    b.append(input ("Digite um número:"))
for i in range (0,n,1):    
    c.append (input ("Digite um número:"))

            



#escreva as demais funções





#escreva o programa principal
