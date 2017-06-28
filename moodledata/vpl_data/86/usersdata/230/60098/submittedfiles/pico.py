# -*- coding: utf-8 -*-

def pico(lista):
    for i in range (0,len(lista)-1,1):
        if lista[i]>lista[i+1]:
            return (i)
    
n = int(input('Digite a quantidade de elementos da lista: '))
a=[]
for i in range(1,n+1,1):
    valor=int(input('Digite o elemento da lista: '))
    a.append(valor)
    
if pico(a):
    print('S')
else:
    print('N')

