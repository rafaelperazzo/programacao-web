# -*- coding: utf-8 -*-
from __future__ import division

def pico(a):
    #CONTINUE...
    
    maior=0
    x=0
    if a[0]<a[1]:
        x=x+1
    for i in range(0,len(a)-1,1):
        if a[i]>a[i+1]:
            maior=a[i]
            break
    
    cont=0
    
    for i in range (maior, len(a)-1,1):
        if a[i]<=a[i+1]:
            cont=cont+1
            
    if maior!=0 and cont==0 and x==1:
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