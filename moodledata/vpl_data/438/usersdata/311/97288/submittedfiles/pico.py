# -*- coding: utf-8 -*-

def pico(lista):
    if n==3:
        if lista[0]<lista[1] and lista[2]<lista[1]:
            return 'S'
        else:
            return 'N'
    if n>3:
        if lista[0]<lista[1] and lista[1]<lista[2]:
            return 'S'
        if lista[0]<lista[1] and lista[n-1]<lista[n-2]:
            return 'S'
        if lista[0]>lista[1]:
            return 'N'
            


n = (int(input('Digite a quantidade de elementos da lista: ')))

a=[]
for i in range (0,n,1):
    a.append(int(input('Digite o numero: ')))

print (pico(a))
