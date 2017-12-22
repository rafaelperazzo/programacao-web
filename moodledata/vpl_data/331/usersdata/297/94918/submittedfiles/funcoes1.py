# -*- coding: utf-8 -*-
n=int(input('digite o numero de elementos que as tres listas possuiram: '))
a=[]
b=[]
c=[]
for i in range(0,n,1):
    a.append(int(input('digite um elemento da lista a: ')))
for i in range(0,n,1):
    b.append(int(input('digite um elemento da lista b: ')))
for i in range(0,n,1):
    c.append(int(input('digite um elemento da lista c: ')))
g=a
def crescente (g):
    r=0
    #escreva o código da função crescente aqui
    for i in range(0,n-1,1):
        if g[i]<g[i+1]:
            r=r+1
        else :
            break
    return r
#escreva as demais funções
def decrescente(g):
    s=0
    for i in range(0,n-1,1):
        if g[i]>g[i+1]:
            s=s+1
        else:
            break
    return s
def elemconsc(g):
    t=0
    for i in range(0,n-1,1):
        if g[i]==g[i+1]:
            t=t+1
            break
    return t
#escreva o programa principal
g=a
ra=crescente(g)
sa=decrescente(g)
ta=elemconsc(g)
if ra==(n-1):
    print('S')
else :
    print('N')
if sa==(n-1) :
    print('S')
else :
    print('N')
if ta>0:
    print('S')
else :
    print('N')
#codigodalista2
g=b
rb=crescente(g)
sb=decrescente(g)
tb=elemconsc(g) 
if rb==(n-1) :
    print('S')
else :
    print('N')
if sb==(n-1) :
    print('S')
else :
    print('N')
if tb>0:
    print('S')
else :
    print('N')
#codigodalista3
g=c
rc=crescente(g)
sc=decrescente(g)
tc=elemconsc(g)
if rc==(n-1):
    print('S')
else :
    print('N')
if sc==(n-1) :
    print('S')
else :
    print('N')
if tc>0:
    print('S')
else :
    print('N')