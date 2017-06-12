# -*- coding: utf-8 -*-
def semelhantes(lista1,lista2):
    total=0
    for i in range(0,len(lista1),1):
        if lista1[i] in lista2:
            total=total+1
    return (total)

n1=int(input('Informe o número de termos da lista1: '))
n2=int(input('Informe o número de termos da lista2: '))
lista1=[]
lista2=[]

for i in range(0,n1,1):
    elemento1=int(input('Informe os elementos da lista1: '))
    lista1.append(elemento1)

for i in range(0,n2,1):
    elemento2=int(input('Informe os elementos da lista2: '))
    lista2.append(elemento2)

total = semelhantes(lista1,lista2)
print(total)