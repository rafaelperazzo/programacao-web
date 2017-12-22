# -*- coding: utf-8 -*-
n=int(input('digite o numero de elementos que as tres listas possuiram: '))
a=[]
b=[]
c=[]
r=0
s=0
t=0
for i in range(0,n,1):
    a.append(int(input('digite um elemento da lista a: ')))
for i in range(0,n,1):
    b.append(int(input('digite um elemento da lista b: ')))
for i in range(0,n,1):
    c.append(int(input('digite um elemento da lista c: ')))
g[i]=a[i]
def crescente (r):
    #escreva o código da função crescente aqui
    for i in range(0,n-1,1):
        if g[i]<g[i+1]:
            r=r+1
    return r
#escreva as demais funções
def decrescente(s):
    for i in range(0,n-1,1):
        if g[i]>g[i+1]:
            s=s+1
    return s
def elemconsc(t):
    for i in range(0,n-1,1):
        if g[i]==g[i+1]:
            t=t+1
    return t
#escreva o programa principal
r=0
s=0
g[i]=a[i]
if crescente(g[i])==n-1 and r==0:
    print('S')
else :
    print('N')
if decrescente(g[i])==n-1 and s==0 :
    print('S')
else :
    print('N')
if elemconsc(g[i])>0 and t>0:
    print('S')
else :
    print('N')
#codigodalista2
r=0
t=0
g[i]=b[i]
if crescente(g[i])==n-1 and r==n :
    print('S')
else :
    print('N')
if decrescente(g[i])==n-1 and s==n :
    print('S')
else :
    print('N')
if elemconsc(g[i])>0 and t>0:
    print('S')
else :
    print('N')
#codigodalista3
r=0
s=0
g[i]=c[i]
if crescente(g[i])==n-1 and r==n:
    print('S')
else :
    print('N')
if decrescente(g[i])==n-1 and s==n :
    print('S')
else :
    print('N')
if elemconsc(g[i])>0 and t>0:
    print('S')
else :
    print('N')