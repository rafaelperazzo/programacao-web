# -*- coding: utf-8 -*-

def pico(lista):
    cont_crescente = 0
    cont_decrescente = 0
    for i in range (0,len(lista)-1,1):
        if lista[i]<lista[i+1]:
            cont_crescente = cont_crescente + 1
        else:
            break
    for i in range (cont_crescente,len(lista) - 1, 1):
        if lista[i]>lista[i+1]:
            cont_decresente = cont_decrescente + 1
        else:
            break
    if cont_crescente + cont_decrescente == len(lista) - 1 and cont_decrescente>0 and cont_crescente>0:
        return ("S")
    else:
        return ("N")
    
lista = []
n = int(input('Digite a quantidade de elementos da lista: '))
for i in range (0,n,1):
    lista.append(int(input("Digite o valor do %dº elemento: "%(i+1))))
print(pico(lista))
#CONTINUE...
