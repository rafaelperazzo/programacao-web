# -*- coding: utf-8 -*-
m=[]
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
for i in range (0,n,1):
    if i+2<n:
        if lista_L[i]!=lista_L[i+1] or lista_L[i]!=lista_L[i+2]:
            diferente_L=lista_L[i]
            indice_dL=i
        if lista_C[i]!=lista_C[i+1] or lista_C[i]!=lista_C[i+2]:
            diferente_C=lista_C[i]
            indice_dC=i
    if i+2>=n:
        break
    if n=2:
        diferente_L=lista_L[0]
        indice_dL=0
        diferente_C=lista_C[0]
        indice_dC=0
if i in range (0,n,1):
    if i+2<n:
        if lista_L[i]==lista[i+1] or lista_L[i]==lista_L[i+2]:
            igual_L=lista_L[i]
            indice_iL=i
        if lista_C[i]==lista_C[i+1] or lista_C[i]==lista_C[i+2]:
            igual_C=lista_C[i]
            indice_iC=i
    if i+2>=n:
        break
    if n=2:
        diferente_L=lista_L[0]
        indice_iL=0
        diferente_C=lista_C[0]
        indice_iC=0
print(m[indice_dL][indice_dC])
resultado=soma_L-n*lista_L[indice_iL]
print(resultado)