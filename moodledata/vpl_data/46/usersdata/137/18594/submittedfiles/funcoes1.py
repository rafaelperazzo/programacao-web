# -*- coding: utf-8 -*-
from __future__ import division

def crescente (a):
    cont=0
    for i in range (0,len(a)-1,1):
        if a[i]>a[i+1]:
            cont=cont+1
    if cont==0:
        return True
    else:
        return False

def decrescente (a):
    cont=0
    for i in range (0,len(a)-1,1):
        if a[i]>a[i+1]:
            cont=cont+1
    if cont!=0:
        return True
    else:
        return False

def consecutivo (a):
    cont=0
    for i in range (0,len(a)-1,1):
        if a[i]==a[i+1]:
            cont=cont+1
    if cont!=0:
        return True
    else:
        return False
def crescente (b):
    cont=0
    for i in range (0,len(b)-1,1):
        if b[i]>b[i+1]:
            cont=cont+1
    if cont==0:
        return True
    else:
        return False

def decrescente (b):
    cont=0
    for i in range (0,len(b)-1,1):
        if b[i]>b[i+1]:
            cont=cont+1
    if cont!=0:
        return True
    else:
        return False

def consecutivo (b):
    cont=0
    for i in range (0,len(a)-1,1):
        if b[i]==b[i+1]:
            cont=cont+1
    if cont!=0:
        return True
    else:
        return False

def crescente (c):
    cont=0
    for i in range (0,len(c)-1,1):
        if c[i]>c[i+1]:
            cont=cont+1
    if cont==0:
        return True
    else:
        return False

def decrescente (c):
    cont=0
    for i in range (0,len(a)-1,1):
        if c[i]>c[i+1]:
            cont=cont+1
    if cont!=0:
        return True
    else:
        return False

def consecutivo (c):
    cont=0
    for i in range (0,len(a)-1,1):
        if c[i]==c[i+1]:
            cont=cont+1
    if cont!=0:
        return True
    else:
        return False
n=input ('n:')
a=[]
b=[]
c=[]
for i in range(0,n,1):
    a.append (input('a:'))

if crescente (a):
    print ('S')
else:
    print ('N')
    
for i in range(0,n,1):
    a.append (input('a:'))

if decrescente (a):
    print ('S')
else:
    print ('N')
    
for i in range(0,n,1):
    a.append (input('a:'))

if consecutivo (a):
    print ('S')
else:
    print ('N')

for i in range(0,n,1):
    b.append (input('b:'))

if crescente (b):
    print ('S')
else:
    print ('N')
    
for i in range(0,n,1):
    b.append (input('b:'))

if decrescente (b):
    print ('S')
else:
    print ('N')
    
for i in range(0,n,1):
    b.append (input('b:'))

if consecutivo (b):
    print ('S')
else:
    print ('N')

for i in range(0,n,1):
    c.append (input('c:'))

if crescente (c):
    print ('S')
else:
    print ('N')
    
for i in range(0,n,1):
    c.append (input('c:'))

if decrescente (c):
    print ('S')
else:
    print ('N')
    
for i in range(0,n,1):
    c.append (input('c:'))

if consecutivo (c):
    print ('S')
else:
    print ('N')

    

        


#escreva as demais funções





#escreva o programa principal
