# -*- coding: utf-8 -*-
n=int(input('digite um valor de elementos:'))
def somatorioi(lista):
    for i in range(0,len(lista),1):
        soma=0
        if lista[i]%2!=0:
            soma=soma+lista[i]
    return(soma)
    
def np(lista):
    for i in range(0,len(lista),1):
        cont=0
        if lista[i]%2==0:
            cont=cont+1
    return(cont)
    
def somatoriop(lista):
    for i in range(0,len(lista),1):
        soma=0
        if lista[i]%2==0:
            soma=soma+lista[i]
    return(soma)

def ni(lista):
    for i in range(0,len(lista),1):
        cont=0
        if lista[i]%2!=0:
            cont=cont+1
    return(cont)
    
a=[]

for i in range(0,n+1,1):
    elemento1=int(input('digite o elemento:'))
    a.append(elemento1)
    
print(somatorioi(a))
print(somatoriop(a))
print(ni(a))
print(np(a))
print(a)















