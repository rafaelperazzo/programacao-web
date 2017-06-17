# -*- coding: utf-8 -*-
n=int(input('digite n:'))
a=[]
for i  in range(0,n,1):
    x=float(input('digite x:'))
    a.append(x)
b=[]
for i  in range(0,n,1):
    y=float(input('digite y:'))
    b.append(y)
c=[]
for i  in range(0,n,1):
    z=float(input('digite :'))
    c.append(z)
def crescente (lista):
    cont=0
    for i in range(1,len(lista),1):
        if lista[i]>lista[i-1]:
            cont=cont+1
    if cont==len(lista)-1:
        return True
    else:
        return False
def decrescente (lista):
    cont=0
    for i in range(1,len(lista),1):
        if lista[i]<lista[i-1]:
            cont=cont+1
    if cont==len(lista)-1:
        return False
    else:
        return True
def consecutivos (lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista==lista[i+1]:
            cont=cont+1
    if cont==0:
        return False
    else:
        return True