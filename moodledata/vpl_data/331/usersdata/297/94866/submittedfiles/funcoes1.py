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
r=0
s=0
t=0
a[i]=[i]
if crescente(r)==0 and crescente(r)==n and elemconsc(t)==0 :
    print('S')
else :
    print('N')
if decrescente(s)==0 and decrescente(s)==n and elemconsc(t)==0 :
    print('S')
else :
    print('N')
if elemconsc(t)>0:
    print('S')
else :
    print('N')
#codigodalista2
r=0
s=0
t=0
b[i]=[i]
if crescente(r)==0 and crescente(r)==n and elemconsc(t)==0 :
    print('S')
else :
    print('N')
if decrescente(s)==0 and decrescente(s)==n and elemconsc(t)==0 :
    print('S')
else :
    print('N')
if elemconsc(t)>0:
    print('S')
else :
    print('N')
#codigodalista3
r=0
s=0
t=0
c[i]=[i]
if crescente(r)==n and crescente(r)==n and elemconsc(t)==0 :
    print('S')
else :
    print('N')
if decrescente(s)==n and decrescente(s)==n and elemconsc(t)==0:
    print('S')
else :
    print('N')
if elemconsc(t)>0:
    print('S')
else :
    print('N')