# -*- coding: utf-8 -*-

def elementos(lista1,lista2):
    cont=0
    for i in range (0,len(lista1),1):
        for j in range (0,len(lista2),1):
            if (lista1[i]==lista2[j]):
                cont=cont+1
    return(cont)            

n=int(input('Digite o número de elementos da lista 1: '))
m=int(input('Digite o número de elementos da lista 2: '))
a=[]
b=[]
for i in range (0,n,1):
    a.append(int(input('Digite o valor (lista 1): ')))
for j in range (0,m,1):
    b.append(int(input('Digite o valor (lista 2): ')))

print(elementos(a,b))

    
