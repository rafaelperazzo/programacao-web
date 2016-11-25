# -*- coding: utf-8 -*-
from __future__ import division

def crescente (a):
    cont=0
    for i in range(0,len(a),1):
        if a[i]<a[i+1]:
            cont = cont + 1
                
    if cont==len(a)-1:
        
        return True #As palavras True e False sempre começam com maiusculas!
    else:
        return False

def decrescente(a):
    cont=0
    for i in range(0,len(a),1):
        if a[i]=a[i+1]:
            return True
        else:
            return False
    
            
       
                
    if cont==len(a)-1:
        return True
    else:
        return False

def consecutivos (a):
    cont=0
    for i in range(0,len(a),1):
        if a[i]=a[i+1]:
            return True
        else:
            return False
        
       
                
    if cont>0:
        return True
    else:
        return False
        
a=[]
b=[]
c=[]

n=int(input('número de termos:'))
for i in range(0,n,1):
    a.append(input('valores a lista de a:'))
for i in range(0,n,1):
    b.append(input('valores a lista de b:'))
for i in range(0,n,1):
    c.append(input('valores a lista de c:'))

if crescente (a):
    print ('S')
else:
    print ('N')
if decrescente (a):
    print ('S')
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
    print ('S')
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
    print ('S')
else:
    print ('N')
if consecutivo (c):
    print ('S')
else:
    print ('N')

