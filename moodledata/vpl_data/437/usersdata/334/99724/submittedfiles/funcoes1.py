# -*- coding: utf-8 -*-

def crescente (lista):
    if [i]<[i+1]:
        print('S')
        print('N')
        print('N')

#escreva as demais funções
def decrescente (lista):
    if [i]>[i-1]:
        print('N')
        print('S')
        print('N')

#escreva o programa principal
n = int(input('Número de elementos: '))
lista1 = []
for i in range (0,n,1):
    lista1.append(int(input('Valores da lista 1 %d: ' % (i+1))))
lista2 = []
for i in range (0,n,1):
    lista2.append(int(input('Valores da lista 2 %d: ' % (i+1))))
lista3 = []
for i in range (0,n,1):
    lista2.append(int(input('Valores da lista 3 %d: ' % (i+1))))

print(crescente)
print(decrescente)