# -*- coding: utf-8 -*-
from __future__ import division

def crescente(a):
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
        return True
        
    else:
        return False


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
        return True
        
    else:
        return False   
        
def continuo(a):
    cont=0
    fo i in range(0,len(a),1):
        if i==0:
            if a[0]=a[1]:
                cont=cont+1
        elif i==len(a)-1:
            if a[len(a)-1]=a[len(a)-2]:
                cont=cont+1
        else:
            if a[i]=a[i+1]:
                cont=cont+1
                
    if cont>0:
        return True
        
    else:
        return False
        
#Entrada

a=[]
b=[]
c=[]

n=int(input('digite o número de termos:'))

for i in range(0,n,1):
    a.append(input('Acrescente valores a lista a:'))
for i in range(0,n,1):
    b.append(input('Acrescente valores a lista b:'))
for i in range(0,n,1):
    c.append(input('Acrescente valores a lista c:'))
    


if decrescente (a):
    print ('S')
else:
    print ('N')
if decrescente (b):
    print ('S')
else:
    print ('N')
if decrescente (c):
    print ('S')
else:
    print ('N')

if consecutivos (a):
    print ('S')
else:
    print ('N')
if consecutivos (b):
    print ('S')
else:
    print ('N')
if consecutivos (c):
    print ('S')
else: 
    print ('N')



