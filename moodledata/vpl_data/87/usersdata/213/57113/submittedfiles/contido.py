# -*- coding: utf-8 -*-
def semelhantes(lista1,lista2):
    contador=0
    for i in range(0,len(lista1),1):
        if a[i] in b:
            contador=contador+1
    return (contador)

n1=int(input('Informe o número de termos da lista1: '))
n2=int(input('Informe o número de termos da lista2: '))
lista1=[]
lista2=[]

for i in range(0,n1,1):
    elemento1=int(imput('Informe os elementos da lista1: '))
    lista1.append(elemento1)

for i in range(0,n2,1):
    elemento2=int(imput('Informe os elementos da lista2: '))
    lista1.append(elemento2)

resultado = semelhantes(lista1,lista2)
print(resultado)