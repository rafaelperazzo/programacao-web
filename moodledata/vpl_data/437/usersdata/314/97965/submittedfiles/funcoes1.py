# -*- coding: utf-8 -*-
#escreva o código da função crescente aqui
def crescente(lista):
    menor = lista[0]
    crescente = true
    for i in range(1, lista.length, 1):
        if lista[i] < menor :
            crescente = false
            break
    return crescente
    

            
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
lerLista(b, n, "B")
lerLista(c, n, "C")

imprimeLista(a)
imprimeLista(b)
imprimeLista(c)

if crescente(a):
    print("'S'")
else :
    print("'N'")