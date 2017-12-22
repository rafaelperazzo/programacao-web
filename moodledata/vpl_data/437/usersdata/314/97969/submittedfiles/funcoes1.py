# -*- coding: utf-8 -*-
#escreva o código da função crescente aqui
def crescente(lista):
    menor = lista[0]
    crescente = True
    for i in range(1, len(lista), 1):
        if lista[i] < menor :
            crescente = False
            break
    return crescente

def decrescente(lista):
    maior = lista[0]
    decrescente = True
    for i in range(1, len(lista), 1):
        if lista[i] > maior :
            decrescente = False
            break
    return decrescente


            
#escreva as demais funções
def lerLista(lista, quantidade, letra) :
    for i in range(0, quantidade, 1):
        lista.append(int(input('Digite o {}º elemento da lista {}: ' .format(i+1, letra))))
        
def imprimeLista(lista) :
    print(lista)

n = int(input('Digite n: '))

a = []
b = []
c = []

lerLista(a, n, "A")
imprimeLista(a)

if crescente(a):
    print("'S'")
else :
    print("'N'")