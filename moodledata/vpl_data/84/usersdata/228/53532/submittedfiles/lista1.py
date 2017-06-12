# -*- coding: utf-8 -*-
n=int(input('digite um valor de elementos:'))
def somatoriop(lista):
    for i in range(0,len(lista),1):
        soma=0
        cont=0
        if lista[i]%2==0:
            cont=cont+1
            soma=soma+lista[i]
    return(soma,cont)
    
def somatorioi(lista):
    for i in range(0,len(lista),1):
        soma=0
        cont=0
        if lista[i]%2==1:
            cont=cont+1
            soma=soma+lista[i]
    return(soma,cont)

lista1=[]

for i in range(0,n,'):
    elemento1=int(input('digite o elemento:'))
    lista1.append(elemento1)
    
print(somatoriop(lista))
print(somatorioi(lista))















