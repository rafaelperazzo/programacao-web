# -*- coding: utf-8 -*-
n=int(input('digite o o numero de elementos que as listas terao: '))
a=[]
b=[]
c=[]
for i in range(0,n,1):
    a.append(int(input('digite o elemento %d da lista a: '%(i+1))))
for i in range(0,n,1):
    b.append(int(input('digite o elemento %d da lista b: '%(i+1))))
for i in range(0,n,1):
    c.append(int(input('digite o elemento %d da lista c: '%(i+1))))
def cresc(lista,n):
    cont_lista=0
    for i in range(0,n-1,1):
        if i==0:
            if lista[i]<lista[i+1]:
                cont_lista=cont_lista+1
        elif lista[i-1]<lista[i] and lista[i]<lista[i+1] :
            cont_lista=cont_lista+1
        elif i==(n-1):
            if lista[i]<lista[i+1]:
                cont_lista=cont_lista+1
    return cont_lista
def decresc(lista2,n):
    cont_lista2=0
    for i in range(0,n-1,1):
        if i==0:
            if lista2[i]>lista2[i+1]:
                cont_lista2=cont_lista2+1
        elif lista2[i-1]>lista2[i] and lista2[i]>lista2[i+1] :
            cont_lista2=cont_lista2+1
        elif i==(n-1):
            if lista2[i]>lista2[i+1]:
                cont_lista2=cont_lista2+1
    return cont_lista2
def igual(lista3,n):
    cont_lista3=0
    for i in range(0,n-1,1):
        if i==0:
            if lista3[i]==lista3[i+1]:
                cont_lista3=cont_lista3+1
        elif lista3[i-1]==lista3[i] and lista3[i]==lista3[i+1] :
            cont_lista3=cont_lista3+1
        elif i==(n-1):
            if lista3[i]==lista3[i+1]:
                cont_lista3=cont_lista3+1
    return cont_lista3

var_1=cresc(a,n)
var_2=decresc(a,n)
var_3=igual(a,n)
var_4=cresc(b,n)
var_5=decresb(b,n)
var_6=igual(b,n)
var_7=cresc(c,n)
var_8=decresc(c,n)
var_9=igual(c,n)
if var_1==n-1:
    print('S')
else :
    print('N')
if var_2==n-1:
    print('S')
else :
    print('N')
if var_3>0:
    print('S')
else :
    print('N')
if var_4==n-1:
    print('S')
else :
    print('N')
if var_5==n-1:
    print('S')
else :
    print('N')
if var_6>0:
    print('S')
else :
    print('N')
    if var_7==n-1:
    print('S')
else :
    print('N')
if var_8==n-1:
    print('S')
else :
    print('N')
if var_9>0:
    print('S')
else :
    print('N')