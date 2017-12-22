# -*- coding: utf-8 -*-
n=int(input('digite o o numero de elementos que as listas terao: '))
a=[]
'''b=[]
c=[]'''
for i in range(0,n,1):
    a.append(int(input('digite o elemento %d da lista a: '%(i+1))))
for i in range(0,n,1):
    b.append(int(input('digite o elemento %d da lista b: '%(i+1))))
for i in range(0,n,1):
    c.append(int(input('digite o elemento %d da lista c: '%(i+1))))
def cresc(lista,n):
    cont_a=0
    for i in range(0,n-1,1):
        if i==0:
            if lista[i]<lista[i+1]:
                cont_a=cont_a+1
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
            if lista[i]>lista[i+1]:
                cont_lista2=cont_lista2+1
        elif lista[i-1]>lista[i] and lista[i]>lista[i+1] :
            cont_lista2=cont_lista2+1
        elif i==(n-1):
            if lista[i]>lista[i+1]:
                cont_lista2=cont_lista2+1
    return cont_b
print(cresc(a,n))
print(decresc(a,n))