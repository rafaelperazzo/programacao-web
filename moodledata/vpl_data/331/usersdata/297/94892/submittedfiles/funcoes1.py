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
g=a
def crescente (r):
    #escreva o código da função crescente aqui
    for i in range(0,n-1,1):
        if g[i]<g[i+1]:
            r=r+1
        else :
            break
    return r
#escreva as demais funções
def decrescente(s):
    for i in range(0,n-1,1):
        if g[i]>g[i+1]:
            s=s+1
        else:
            break
    return s
def elemconsc(t):
    for i in range(0,n-1,1):
        if g[i]==g[i+1]:
            t=t+1
            break
    return t
#escreva o programa principal
r=0
s=0
t=0
crescente(g[i])
decrescente(g[i])
elemconsc(g[i])
if r==n:
    print('S')
else :
    print('N')
if s==n :
    print('S')
else :
    print('N')
if t>0:
    print('S')
else :
    print('N')
#codigodalista2
r=0
s=0
t=0
g=b
crescente(g[i])
decrescente(g[i])
elemconsc(g[i]) 
if r==n :
    print('S')
else :
    print('N')
if s==n :
    print('S')
else :
    print('N')
if t>0:
    print('S')
else :
    print('N')
#codigodalista3
r=0
s=0
t=0
g=c
crescente(g[i])
decrescente(g[i])
elemconsc(g[i])
if r==n:
    print('S')
else :
    print('N')
if s==n :
    print('S')
else :
    print('N')
if t>0:
    print('S')
else :
    print('N')