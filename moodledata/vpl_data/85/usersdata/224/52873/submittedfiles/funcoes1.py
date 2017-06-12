
# -*- coding: utf-8 -*-

def cres (k):
    cont=0
    for i in range(0,len(k),1):
        if k[i]<k[i+1]:
            cont=cont+1
    if cont==len(k)-1:
        return True
    else:
        return False
def decre (k):
    cont=0
    for i in range(0,len(k),1):
        if k[i]>k[i+1]:
            cont=cont+1
    if cont==len(k)-1:
        return True
    else:
        return False
def consecutivo(k):
    cont=0
    for i in range(0,len(k),1):
        if k[i+1]-k[i]==1:
            cont=cont+1
    if cont==len(k)-1:
        return True
n=int(input('Digite o tamanho da lista:  '))
g=[]
c=[]
w=[]
for i in range(1,n+1,1):
    x=int(input('Digite os numeros: '))
    g.append(x)
for i in range(1,n+1,1):
    x=int(input('Digite os numeros: '))
    c.append(x)
for i in range(1,n+1,1):
    x=int(input('Digite os numeros: '))
    w.append(x)

if cres(g):
    print('S')
else:
    print('N')

if decre(g):
    print('S')
else:
    print('N')

if consecutivo(g):
    print('S')
else:
    print('N')

if cres(c):
    print('S')
else:
    print('N')

if decre(c):
    print('S')
else:
    print('N')

if consecutivo(c):
    print('S')
else:
    print('N')
    
if cres(w):

    print('S')
else:
    print('N')
if decre(w):
    print('S')
else:
    print('N')
if consecutivo(w):
    print('S')
else:
    print('N')