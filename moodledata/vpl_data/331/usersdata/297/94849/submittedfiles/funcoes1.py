# -*- coding: utf-8 -*-
n=int(input('digite o numero de elementos que as tres listas possuiram: '))
a=[]
b=[]
c=[]
r=0
s=0
t=0
for i in range(0,n,1):
    a.append(int(input('digite um elemento da lista 1: ')))
for i in range(0,n,1):
    b.append(int(input('digite um elemento da lista 2: ')))
for i in range(0,n,1):
    c.append(int(input('digite um elemento da lista 3: ')))
def crescente (r):
    #escreva o código da função crescente aqui
    for i in range(0,n-1,1):
        if i<(i+1):
            r=r+1
    return resultado
#escreva as demais funções
def decrescente(s):
    for i in range(0,n-1,1):
        if i>(i+1):
            s=s+1
    return resultado
def elemconsc(t):
    for i in range(0,n-1,1):
        if i==(i+1):
            t=t+1
    return resultado
#escreva o programa principal
r=(a[i])
s=(a[i])
t=(a[i])
if crescente(a[i])>0:
    print('S')
else :
    print('N')
if decrescente(a[i]):
    print('S')
else :
    print('N')
if elemconsc(a[i]):
    print('S')
else :
    print('N')
cresclist_a=0
decresclist_a=0
elemconsc_a=0
#codigodalista2
r=(b[i])
s=(b[i])
t=(b[i])
if crescente(b[i])>0:
    print('S')
else :
    print('N')
if decrescente(b[i]):
    print('S')
else :
    print('N')
if elemconsc(b[i]):
    print('S')
else :
    print('N')
#codigodalista2
r=(c[i])
s=(c[i])
t=(c[i])
if crescente(c[i])>0:
    print('S')
else :
    print('N')
if decrescente(c[i]):
    print('S')
else :
    print('N')
if elemconsc(c[i]):
    print('S')
else :
    print('N')