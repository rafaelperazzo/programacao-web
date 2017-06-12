# -*- coding: utf-8 -*-
def crescente (lista):
    for i in range (0,len(lista),1):
        if lista[i]>=lista[i+1]:
            return False
    return True

def decrescente (lista):
    for i in range (0,len(lista),1):
        if lista[i]<=lista[i+1]:
            return False
    return True    

def iguais (lista):
    cont=0
    for i in raange (0,len(lista),1):
        if a[i]==a[i+1]:
            cont=cont+1
    if cont==0:
        return False
    else:
        return True

n=int(input('Digite a quantidade de elementos:'))

a=[]
for i in range (0,n,1):
    valor=int(input('Valor:'))
    a.append(valor)

b=[]
for i in range (0,n,1):
    valor=int(input('Valor:'))
    b.append(valor)    

c=[]
for i in range (0,n,1):
    valor=int(input('Valor:'))
    c.append(valor)    

    