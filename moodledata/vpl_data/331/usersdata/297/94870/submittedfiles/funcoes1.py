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
        if [i]<[i+1]:
            r=r+1
    return r
#escreva as demais funções
def decrescente(s):
    for i in range(0,n-1,1):
        if [i]>[i+1]:
            s=s+1
    return s
def elemconsc(t):
    for i in range(0,n-1,1):
        if [i]==[i+1]:
            t=t+1
    return t
#escreva o programa principal
if crescente(a[i])==n and decrescente(a[i])==n and elemconsc(a[i])==0 :
    print('S')
else :
    print('N')
if decrescente(a[i])==n and decrescente(a[i])==n and elemconsc(a[i])==0 :
    print('S')
else :
    print('N')
if elemconsc(a[i])>0:
    print('S')
else :
    print('N')
#codigodalista2
if crescente(b[i])==n and decrescente(b[i])==n and elemconsc(b[i])==0 :
    print('S')
else :
    print('N')
if decrescente(b[i])==n and decrescente(b[i])==n and elemconsc(b[i])==0 :
    print('S')
else :
    print('N')
if elemconsc(b[i])>0:
    print('S')
else :
    print('N')
#codigodalista3
if crescente(c[i])==n and decrescente(c[i])==n and elemconsc(c[i])==0 :
    print('S')
else :
    print('N')
if decrescente(c[i])==n and decrescente(c[i])==n and elemconsc(c[i])==0:
    print('S')
else :
    print('N')
if elemconsc(c[i])>0:
    print('S')
else :
    print('N')