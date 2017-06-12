# -*- coding: utf-8 -*-

def crescente(lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]>lista[i+1]:
            cont=cont+1
    if cont==0:
        return True
    else:
        return False

def decrescente(lista):
    cont=0
    for i in range(1,len(lista),1):
        if lista[i]<lista[i-1]:
            cont=cont+1
    if cont==0:
        return True
    else:
        return False
        
def consecutivos(lista):
    cont=0
    for i in range(0,len(lista),1):
        if i==0:
            if lista[i]==lista[i+1]:
                cont=cont+1
        elif i==len(lista)-1:
            if lista[i]==lista[i-1]:
                cont=cont+1
        else:
            if lista[i]==lista[i+1] or lista[i]==lista[i-1]:
                cont=cont+1
    if cont!=0:
        return True
    else:
        return False

n=int(input('n:'))
a=[]
for i in range(1,n+1,1):
    na=int(input('a:'))
    a.append(na)
b=[]
for i in range(1,n+1,1):
    nb=int(input('b:'))
    b.append(nb)
c=[]
for i in range(1,n+1,1):
    nc=int(input('c:'))
    c.append(nc)
if crescente(a):
    print('S')
else:
    print('N')
if decrescente(a):
    print('S')
else:
    print('N')
if consecutivos(a):
    print('S')
else:
    print('N')
if crescente(b):
    print('S')
else:
    print('N')
if decrescente(b):
    print('S')
else:
    print('N')
if consecutivos(b):
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
if consecutivos(c):
    print('S')
else:
    print('N')