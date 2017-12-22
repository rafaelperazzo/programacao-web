# -*- coding: utf-8 -*-

def pico(lista):
    contagem = 0
    for i in range (0, len(lista)-1):
        if lista[i]<lista[i+1]:
            contagem += 1
        else:
            break
    for i in range (contagem, len(lista)-1):
        if lista[i]>lista[i+1]:
            contagem += 1
        else:
            break
    if contagem == len(lista)-1:
        return 'S'
    else:
        return 'N'
    
lista = []
n = int(input('Digite a quantidade de elementos da lista: '))
for i in range (0, n):
    lista.append(int(input('Insira o valor: ')))

print(pico(lista))
