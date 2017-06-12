# -*- coding: utf-8 -*-

def crescente (lista):
    cont=0
    for i in range(1,len(lista),1):
        if lista[i]>lista[i-1]:
            cont=cont+1
    if cont==len(lista)-1:
        return True
    else:
        return False

def decrescente (lista):
    cont=0
    fo i in range(1,len(lista)1):
        if lista[i]<lista[i-1]:
            cont=cont+1
    if cont==len(lista)-1:
        return True
    else:
        return False
        
def consecutivos(lista):
    cont=0
    for i in range(0,len(lista),1):
        if lista[i]==lista[i+1}:
            cont=cont+1
    if cont==0:
        return False
    else:
        return True

n=int(input('n:'))
a=[]
b=[]
c=[]
for i in range(1,n+1,1):
    numero=float(input('num:'))
    a.append(int(input(numero)))
for i in range(1,n+1,1):
    numero=float(input('num:'))
    b.append(int(input(numero)))
for i in range(1,n+1,1):
    numero=float(input('num:'))
    b.append(int(input(numero)))


