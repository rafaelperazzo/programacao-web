# -*- coding: utf-8 -*-
from __future__ import division

def crescente (lista):
    for i in range (0,n,1):
        if len[i]>len[i+1]:
            return true
        else:
            return false
            
def decrescente (lista):
    for i in range (0,n,1):
        if len[i]<len[i+1]:
            return true
        else:
            return false
            
def consecutivo (lista):
    cont=0
    for i in range (0,n,1):
        if len[i]==len[i+1]:
            cont=cont+1
            if cont>=1:
                return true
            else:
                return false
                
n=input('Digite o valor de n:')
a=[]
b=[]
c=[]

for i in range (0,n,1):
    a.append(input('Digite um valor A:'))
    
for i in range (0,n,1):
    b.append(input('Digite um valor B:'))  
    
for i in range (0,n,1):
    c.append(input('Digite um valor C:'))
    
if crescente (a):
    print ('S')
else:
    print ('N')

if decrescente (a):
    print ('s')
else:
    print ('N')

if consecutivo (a):
    print ('S')
else:
    print ('N')
    
if crescente (b):
    print ('S')
else:
    print ('N')

if decrescente (b):
    print ('s')
else:
    print ('N')

if consecutivo (b):
    print ('S')
else:
    print ('N')
    
if crescente (c):
    print ('S')
else:
    print ('N')

if decrescente (c):
    print ('s')
else:
    print ('N')

if consecutivo (c):
    print ('S')
else:
    print ('N')    
    
    
    
