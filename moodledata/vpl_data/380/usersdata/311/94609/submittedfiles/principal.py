# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
a=[2,1,1]
n=int(input('Digite seu numero: '))
cont= 0
def crescente(lista):

    while (cont<n-1):
        while lista[cont]<lista[cont+1]:
             cont=+1
    if cont==n-1:
        return 'S'
print (crescente(a))