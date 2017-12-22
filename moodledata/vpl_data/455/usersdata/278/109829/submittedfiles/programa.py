# -*- coding: utf-8 -*-
n = int(input('Digite a dimensão da matriz quadrada: '))
for i in range (0,n,1):
    lista=[]
    for j in range (0,n,1):
        lista.append(int(input('Digite o elemento da linha%.d e coluna%.d: ' %(i,j))))
    m.append(lista)
soma_L=0
lista_L=[]
for i in range (0,n,1):
    for j in range (0,n,1):
        soma_L+=m[i][j]
    lista_L.append(soma_L)
soma_C=0
lista_C=[]
for j in range (0,n,1):
    for i in range (0,n,1):
        soma_C+=m[i][j]
    lista_C.append(soma_C)
diferente_L=0
diferente_C=0
for i in range (0,n,1):
    if diferente_L!=lista_L[i]:
        diferente_L=lista_L[i]
        indice_L=i
    if diferente_C!=lista_C[i]:
        diferente_C=lista_C[i]
        indice_L=i
print(m[indice_L][indice_C])
for i in range (0,n,1):
    if i+1<n:
        if lista_L[i]==lista_L[i+1]:
            igual=lista_L[i]
resultado=soma_L-n*lista_L[i]
print(resultado)