# -*- coding: utf-8 -*-
from __future__ import division

def pico(a):
    #CONTINUE...
    
    contC=0
    contD=0
    
    for i in range(0,len(a)-2,1):
        if a[i]<a[i+1]:
            contC=contC+1
        else:
            break
    for i in range(0,len(a)-1,1):
        if a[i]>a[i+1]:
            contD=contD+1
        else:
            break
    
    if contC>0 and contD>0 and contC+contD==len(a)-1:
        return True
    else:
        return False
    
n = input('Digite a quantidade de elementos da lista: ')
#CONTINUE...

a=[]

for i in range(0,n,1):
    a.append(input('Digite um termo: '))

if pico(a):
    print 'S'

else:
    print 'N'