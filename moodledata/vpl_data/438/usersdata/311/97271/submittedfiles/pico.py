# -*- coding: utf-8 -*-

def pico(lista):
    for i in range (0,n,1):
        if lista[1]<lista[2] or lista[n-1]<lista[n-2] and lista[0]<lista[1]:
            return 'S'
        continue
        else:
            return 'N'


n = (int(input('Digite a quantidade de elementos da lista: ')))

a=[]
for i in range (0,n,1):
    a.append(int(input('Digite o numero: ')))

print (pico(a))
