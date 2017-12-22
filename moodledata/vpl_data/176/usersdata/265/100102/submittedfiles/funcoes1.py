# -*- coding: utf-8 -*-
def crescente(d,lista):
    cont=0
    for i in range (0,d-1,1):
        if lista[i]<lista[i+1]:
            cont=cont+1
    if cont==(len(lista)-1):
        return('S')
    else:
        return('N')
        
def decrescente(d,lista):
    cont=0
    for i in range (0,d-1,1):
        if lista[i]>lista[i+1]:
            cont=cont+1
    if cont==(len(lista)-1):
        return('S')
    else:
        return('N')
        
def consecutivo(d,lista):
    cont=0
    for i in range (0,d-1,1):
        if lista[i]==lista[i+1]:
            cont=cont+1
    if cont>0:
        return('S')
    else:
        return('N')
        
n=int(input(digite a quantidade de termos das listas: '))
a=[]
b=[]
c=[]
for i in range(0,n,1):
    valoAr=float(input('digite oa valores da lista a: '))
    a.append(valorA)
for i in range(0,n,1):
    valorB=float(input('digite oa valores da lista b: '))
    b.append(valorB)
for i in range(0,n,1):
    valorC=float(input('digite oa valores da lista c: '))
    c.append(valorC)

print(crescente(n,a))
print(decrescente(n,a))
print(conscutivo(n,a))
