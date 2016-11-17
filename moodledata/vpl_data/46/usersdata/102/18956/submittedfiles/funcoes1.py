# -*- coding: utf-8 -*-
from __future__ import division

def crescente (b):
    cont=0
    for i in range(0,len(b),1):
        if i==0:
            if b[0]<b[1]:
                cont=cont+1
        elif i==len(b)-1:
            if b[len(b)-1]>b[len(b)-2]:
                cont=cont+1
        else:
            if b[i]<b[i+1] and b[i]>b[i-1]:
                cont=cont+1
                
    if cont==len(b):
        return true
    else:
        return false

def decrescente(b):
    cont=0
    for i in range(0,len(b),1):
        if i==0:
            if b[0]>b[1]:
                cont=cont+1
        elif i==len(b)-1:
            if b[len(b)-1]<b[len(b)-2]:
                cont=cont+1
        else:
            if b[i]>b[i+1] and b[i]<b[i-1]:
                cont=cont+1
                
    if cont==len(b):
        return true
    else:
        return false

def consecutivos (b):
    cont=0
    for i in range(0,len(b),1):
        if i==0:
            if b[0]==b[1]:
                cont=cont+1
        elif i==len(b)-1:
            if b[len(b)-1]==b[len(b)-2]:
                cont=cont+1
        else:
            if b[i]==b[i+1] and b[i]==b[i-1]:
                cont=cont+1
                
    if cont==len(b):
        return true
    else:
        return false
        
a=[]
b=[]
c=[]

n=int(input('número de termos:'))
for i in range(0,n,1):
    a.append(input('valores à lista de a:'))
for i in range(0,n,1):
    b.append(input('valores à lista de b:'))
for i in range(0,n,1):
    c.append(input('valores à lista de c:'))

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
    


    
    #escreva o código da função crescente aqui


#escreva as demais funções





#escreva o programa principal
