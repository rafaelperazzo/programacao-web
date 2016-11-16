# -*- coding: utf-8 -*-
from __future__ import division

a=[]
b=[]

n=input("Digite a quantidade de elementos para a:")
m=input("Digite a quantidade de elementos para b:")

for i in range (0,n,1):
    a.append(input("Digite um elemento para a:"))
    
for i in range (0,m,1):
    b.append(input("Digite um elemento para b:"))
cont=0
def funcao (a,b):
    cont=0
    for i in range (1,len(b)-1,1):
        if b[i] in a:
            cont=cont+1
        
         
    return cont
    
print cont