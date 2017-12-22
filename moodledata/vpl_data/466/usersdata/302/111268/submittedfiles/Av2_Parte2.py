# -*- coding: utf-8 -*-
def crescente(lista):
    if sorted(lista) == lista:
        return print('S')
    else:
        return print('N')
def decrescente(lista):
    if sorted(lista, reverse = True) == lista:
        return print('S')
    else:
        return print('N')
        
n = int(input('Digite a quantidade de elementos: '))
a = []
b = []
c = []
for i in range(n):
    a.append(int(input('Digite o elemento %d de a: '%(i+1))))
for i in range(n):
    b.append(int(input('Digite o elemento %d de b: '%(i+1))))    
for i in range(n):
    c.append(int(input('Digite o elemento %d de c: '%(i+1))))
crescente(a)
