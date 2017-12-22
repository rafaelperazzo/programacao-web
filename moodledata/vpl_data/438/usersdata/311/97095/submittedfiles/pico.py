# -*- coding: utf-8 -*-

def pico(lista):
    for i in range (0,n,1):
        if lista[i]<lista[i+1]<lista[i+2] and lista[n-1]<lista[n-2]<lista[n-3]:
            return 'S'
        else:
            return 'N'


n = (int(input('Digite a quantidade de elementos da lista: ')))

a=[]
for i in range (0,n,1):
    a.append(int(input('Digite o numero: ')))

print (pico(a))
