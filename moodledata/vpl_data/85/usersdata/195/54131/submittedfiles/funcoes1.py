# -*- coding: utf-8 -*-
def crescente (k):
    cont=0
    for i in range(0,len(k),1):
        if k[i]>k[i-1]:
            cont=cont+1
    if cont==len(k)-1:
        return True
    else:
        return False
        
def decrescente (k):
    cont=0
    for i in range(0,len(k),1):
        if k[i]<k[i-1]:
            cont=cont+1
    if cont==len(k)-1:
        return True
    else:
        return False
        
def consecutivo (k):
    cont=0
    for i in range(0,len(k),1):
        if i==0:
            if k[i]==k[i+1]:
                cont=cont+1
        elif i==len(k)-1:
            if k[i]==k[i-1]:
                cont=cont+1
        else:
            if k[i]==k[i+1] or k[i]==k[i-1]:
                cont=cont+1
    if cont!=0:
        return True
    else:
        return False
        
n=int(input('digite o tamanho da lista:'))
g=[]
c=[]
w=[]
for i in range(1,n+1,1):
    x=int(input('digite os numeros:'))
    g.append(x)
for i in range(1,n+1,1):
    x=int(input('digite os numeros:'))
    c.append(x)
for i in range(1,n+1,1):
    x=int(input('digite os numeros:'))
    w.append(x)
if crescente(g):
    print('S')
else:
    print('N')
if decrescente(g):
    print('S')
else:
    print('N')
if consecutivo(g):
    print('S')
else:
    print('N')
if crescente(c):
    print('S')
else:
    print('N')
if decrescente(c):
    print('S')
else:
    print('N')
if consecutivo(c):
    print('S')
else:
    print('N')
if crescente(w):
    print('S')
else:
    print('N')
if decrescente(w):
    print('S')
else:
    print('N')
if consecutivo(w):
    print('S')
else:
    print('N')