# -*- coding: utf-8 -*-
from __future__ import division

def crescente (a):
    cont=0
    for i in range(0,len(a),1):
        if i==0:
            if a[0]<a[1]:
                cont=cont+1
        elif i==len(a)-1:
            if a[len(a)-1]>a[len(a)-2]:
                cont=cont+1
        else:
            if a[i]<a[i+1] and a[i]>a[i-1]:
                cont=cont+1
                
    if cont==len(a):
        
        return true
    else:
        return false

def decrescente(a):
    cont=0
    for i in range(0,len(a),1):
        if i==0:
            if a[0]>a[1]:
                cont=cont+1
        elif i==len(a)-1:
            if a[len(a)-1]<a[len(a)-2]:
                cont=cont+1
        else:
            if a[i]>a[i+1] and a[i]<a[i-1]:
                cont=cont+1
                
    if cont==len(a):
        return true
    else:
        return false

def consecutivos (a):
    cont=0
    for i in range(0,len(a),1):
        if i==0:
            if a[0]==a[1]:
                cont=cont+1
        elif i==len(a)-1:
            if a[len(a)-1]==a[len(a)-2]:
                cont=cont+1
        else:
            if a[i]==a[i+1]:
                cont=cont+1
                
    if cont>0:
        return true
    else:
        return false
        
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

