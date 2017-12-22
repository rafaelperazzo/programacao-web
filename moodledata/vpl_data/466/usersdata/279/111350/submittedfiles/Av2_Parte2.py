# -*- coding: utf-8 -*-

n1=(int(input()))
n2=(int(input()))
n3=(int(input()))
lista1=[]
lista2=[]
lista3=[]
for i in range (0,n1,1) :
    lista1.append(int(input()))
for i in range (0,n2,1) :    
    lista2.append(int(input()))
for i in range (0,n3,1) :
    lista3.append(int(input()))

def ordemlista (lista) :
    a=0
    b=0
    c=0
    for i in range(0,len(lista)-1,1) :
        if lista[i]<lista[i+1] :
            a=a+1
        if lista[i]>lista[i+1] :
            b=b+1
        if lista[i]==lista[i+1] :
            c=c+1
    if (a==(len(lista)-2)) :
        print('S')
    else:
        print('N')
    if (b==(len(lista)-2)) :
        print('S')
    else:
        print('N')
    if c!=0 : 
        print('S')
    else:
        print('N')
    return    

ordemlista(lista1)
ordemlista(lista2)
ordemlista(lista3)

























