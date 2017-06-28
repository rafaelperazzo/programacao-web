# -*- coding: utf-8 -*-
def crescente(x):
    cont=0
    for i in range(0,len(x),1):
        if x[i]>x[i-1]:
            cont=cont+1
    if cont==len(x)-1:
        return(True)
    else:
        return(False)

def decrescente(y):
    cont=0
    for i in range(1,len(y),1):
        if y[i]<y[i-1]:
            cont=cont+1
    if cont==len(y)-1:
        return(True)
    else:
        return(False)

def consecutivo(z):
    cont=0
    for i in range(0,len(z),1):
        if i==0:
            if z[i]==z[i+1]:
                cont=cont+1
        elif i==len(z)-1:
            if z[i]==z[i-1]:
                cont=cont+1
        else:
            if z[i]==z[i+1] or z[i]==z[i-1]:
                cont=cont+1
    if cont!=0:
        return True
    else:
        return False
    
n=int(input('digite o tamanho da lista:'))
a=[]
b=[]
c=[]
for i in range(1,n+1,1):
    k=int(input('digite os numeros:'))
    a.append(k)
for i in range(1,n+1,1):
    l=int(input('digite os numeros:'))
    b.append(l)
for i in range(1,n+1,1):
    m=int(input('digite os numeros:'))
    c.append(m)
if crescente(a):
    print('S')
else:
    print('N')
if decrescente(a):
    print('S')
else:
    print('N')
if consecutivo(a):
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
if consecutivo(b):
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
