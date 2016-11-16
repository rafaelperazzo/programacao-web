# -*- coding: utf-8 -*-
from __future__ import division

def pico(a):
   ppico=0
    for i in range (0,len(a)-1,1):
        if a[i]>a[i+1]:
            ppico=i
            break 
        if ppico!=0:
            cont=0
        for i in range (ppico,len(a)-1,1):
            if a[i]<=[i+1]:
                cont=cont+1
                
    
for i in range(0,n,1):
    a.append(input("Digite os elementos da lista: "))
    

    
n = input('Digite a quantidade de elementos da lista: ')
#CONTINUE...
