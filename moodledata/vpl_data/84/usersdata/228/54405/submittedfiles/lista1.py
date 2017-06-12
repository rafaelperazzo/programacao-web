# -*- coding: utf-8 -*-
n=int(input('digite um valor de elementos:'))
def somatoriop(lista):
    for i in range(0,len(lista),1):
        soma=0
        cont=0
        if lista[i]%2==0:
            cont=cont+1
            soma=soma+lista[i]
    return(soma)
    
def np(lista):
    for i in range(0,len(lista),1):
        soma=0
        cont=0
        if lista[i]%2==0:
            cont=cont+1
            soma=soma+lista[i]
    return(cont)
    
def somatorioi(lista):
    for i in range(0,len(lista),1):
        soma=0
        cont=0
        if lista[i]%2==1:
            cont=cont+1
            soma=soma+lista[i]
    return(soma)

def ni(lista):
    for i in range(0,len(lista),1):
        soma=0
        cont=0
        if lista[i]%2==1:
            cont=cont+1
            soma=soma+lista[i]
    return(cont)
    
lista=[]

for i in range(0,n,1):
    elemento1=int(input('digite o elemento:'))
    lista.append(elemento1)
    
print(somatorioi(lista))
print(somatoriop(lista))
print(ni(lista))
print(np(lista))
for i in range(0,len(lista),1):
    ind=lista[i]
    print(ind)















