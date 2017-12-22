# -*- coding: utf-8 -*-
n=int(input('digite o numero de elementos que irao compor as listas; '))
lista1=[]
lista2=[]
for i in range(n):
    lista1.append(int(input('digite o %d elemento que compora a lista1: '%(i+1))))
for i in range(n):
    lista2.append(int(input('digite o %d elemento que compora a lista2: '%(i+1))))
def lecker(lista,n):
    cont=0
    for i in range(1,n-1,1):
        if i==1:
            if lista[i]>lista[i+1]:
                cont=cont+1
        elif i==n-1:
            if lista[i]>lista[i-1]:
                cont=cont+1
        else :
            if lista[i]>lista[i+1] and lista[i]>lista[i-1]:
                cont=cont+1
    if cont==1:
        return True
    else:
        return False
if lecker(lista1,n):
    print('S')
else :
    print('N')
if lecker(lista2,n):
    print('S')
else :
    print('N')