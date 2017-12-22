# -*- coding: utf-8 -*-
n=int(input('digite o numero de elementos que as tres listas possuiram: '))
a=[]
b=[]
c=[]
cresclist_a=0
decresclist_a=0
elemconsc_a=0
for i in range(0,n,1):
    a.append(int(input('digite um elemento da lista 1: ')))
for i in range(0,n,1):
    b.append(int(input('digite um elemento da lista 2: ')))
for i in range(0,n,1):
    c.append(int(input('digite um elemento da lista 3: ')))
def crescente (cresclist_a):
    #escreva o código da função crescente aqui
    for i in range(0,n-1,1):
        if i<(i+1):
            cresclist_a=cresclist_a+1
    return resultado
#escreva as demais funções
def decrescente(decresclist_a):
    for i in range(0,n-1,1):
        if i>(i+1):
            decresclist_a=decresclist_a+1
    return resultado
def elemconsc(elemconsc_a):
    for i in range(0,n-1,1):
        if i==(i+1):
            elemconsc_a=elemconsc_a+1
    return resultado
#escreva o programa principal
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
cresclist_a=0
decresclist_a=0
elemconsc_a=0
#codigodalista2
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