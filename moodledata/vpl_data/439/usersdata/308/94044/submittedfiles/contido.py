# -*- coding: utf-8 -*-
def contido(lista1, lista2):
    contagem = 0
    for i in lista1:
        for j in lista2:
            if i==j:
                contagem += 1
    
    return contagem


l1 = []
l2 = []
n1 = int(input('Informe N1: '))
n2 = int(input('Informe N2: '))
for i in range (0, n1):
    l1.append(int(input('Informe l1: ')))
for i in range (0, n2):
    l2.append(int(input('Informe l1: ')))

print(contido(l1, l2))
