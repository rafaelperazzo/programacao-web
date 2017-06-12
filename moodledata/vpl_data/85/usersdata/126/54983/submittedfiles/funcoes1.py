# -*- coding: utf-8 -*-
p=[]
q=[]
r=[]
i=0
n=int(input('digite n:'))


for i in range(0,n,1):
    valor=float(input('digite o valor da primeira lista:'))
    p.append(valor)
    i=i+1
    
for i in range(1,n+1,1):
    valor=float(input('digite o valor da segunda lista:'))
    q.append(valor)
    i=i+1
    
for i in range(1,n+1,1):
    valor=float(input('digite o valor da terceira lista:'))
    r.append(valor)
    i=i+1

def crescente (a):
    cont=0
    i=0
    for i in range(1,len(a)-1,1):
        if a[i]<a[i+1]:
            cont=cont+1
            i=i+1
    if cont==(len(a)):
        return True
def decrecente (a):
    cont=0
    i=0
    for i in range(1,len(a)-1,1):
        if a[1]>a[i+1]:
            cont=cont+1
            i=i+1
    if cont==(len(a)):
        return True
def consecutivosiguais (a):
    cont=0
    i=0
    for i in range(1,len(a)-1,1):
        if a[i]==a[i+1]:
            cont=cont+1
            i=i+1
    if cont>0:
        return True


if crescente(p):
    print('S')
else:
    print('N')
if decrecente(p):
    print('S')
else:
    print('N')
if consecutivosiguais(p):
    print('S')
else:
    print('N')
if crescente(q):
    print('S')
else:
    print('N')
if decrecente(q):
    print('S')
else:
    print('N')
if consecutivosiguais(q):
    print('S')
else:
    print('N')
    
if crescente(r):
    print('S')
else:
    print('N')
if decrecente(r):
    print('S')
else:
    print('N')
if consecutivosiguais(r):
    print('S')
else:
    print('N')






