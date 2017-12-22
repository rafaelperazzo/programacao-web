# -*- coding: utf-8 -*-

def pico(lista):

    for i in range(0,n,1):
        if lista[0]<lista[1] and lista[n-1]<lista[n-2]:
            return 'S'
        else:
            return 'N'


n = (input('Digite a quantidade de elementos da lista: '))

a=[]
for i in range (0,n,1):
    a.append(input('Digite o numero: '))

print (pico(a))
