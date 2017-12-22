# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
a=[2,1,1]
n=int(input('Digite seu numero: '))
i = 0
def crescente(lista,i):

    while (i<n-1):
        while lista[i]<lista[i+1]:
             i=+1
    if i==n-1:
        return 'S'
print (crescente(a))