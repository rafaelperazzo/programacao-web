# -*- coding: utf-8 -*-
n=int(input('digite um valor de elementos:'))
def somatorioi(a):
    for i in range(0,len(a),1):
        soma=0
        if lista[i]%2!=0:
            soma=soma+lista[i]
    return(soma)
    
def np(lista):
    for i in range(0,len(a),1):
        cont=0
        if lista[i]%2==0:
            cont=cont+1
    return(cont)
    
def somatoriop(a):
    for i in range(0,len(a),1):
        soma=0
        if lista[i]%2==0:
            soma=soma+lista[i]
    return(soma)

def ni(a):
    for i in range(0,len(a),1):
        cont=0
        if lista[i]%2!=0:
            cont=cont+1
    return(cont)
    
lista=[]

for i in range(0,n+1,1):
    elemento1=int(input('digite o elemento:'))
    lista.append(elemento1)
    
print(somatorioi(lista))
print(somatoriop(lista))
print(ni(lista))
print(np(lista))
print(lista)















