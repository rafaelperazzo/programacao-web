# -*- coding: utf-8 -*-

def pico(lista):
    a=(len(lista)+1)/2
    for i in range(1,a,1):
        if lista[i]<lista[i-1]:
            resturn False
    for i in range(a-1,len(lista)-1,1):
        if lista[i]<lista[i+1]:
            return False
    return True
n = input('Digite a quantidade de elementos da lista: ')
lista=[]
for i in range(n):
    a=int(input('a: '))
    lista.append(a)
if pico(lista):
    print('S')
else: 
    print('N')