# -*- coding: utf-8 -*-

def pico(a):
    cont=0
    cont1=0
    i=0
    for i in range(0,len(a)-1,1):
        while a[i]<a[i+1]:
            cont=cont+1
            i=i+1
    for i in range(cont,len(a)-1,1):
        while a[i]>a[i+1]:
            cont1=cont1+1
    if cont1==(len(a)-1):
        return True

n = int(input('Digite a quantidade de elementos da lista: '))
a=[]
i=0
for i in range(0,n,1):
    p=int(input('digite um valor:'))
    a.append(p)
    i=i+1

if pico(a):
    priint('S')
else:
    print('N')
