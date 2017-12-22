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
def consecutivo(lista):
    cont = 0
    for i in range(1,n):
        if lista[i-1] == lista[i]:
          cont += 1
    if cont == 0:
        return print('N')
    else:
        return print('S')
        
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
decrescente(a)
consecutivo(a)
