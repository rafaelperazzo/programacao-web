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
l=lista_L[0]
cont_L=0
indice_L=0
erro=0
certo=0
for i in range (0,n,1):
    if lista_L[i] in l:
        continue
    else:
        cont_L+=1
        indice_L=i
if cont_L==1:
    erro=lista_L[indice_L]
    certo=lista_L[0]
if cont_L!=1:
    erro=lista_L[0]
    certo=lisat_L[1]
c=soma_C[0]
cont_C=0
erro_C=0
for i in range (0,n,1):
    if lista_C[i] in c:
        continue
    else:
        cont_C+=1
        indice_C=i
if cont_C==1:
    erro_C=lista_C[indice_C]
if cont_C!=1:
    erro_C=lista_C[0]
    indice_C=0
inicial=certo-(erro-m[indice_L][indice_C]
final=m[indice_L][indice_C]
print(inicial)
print(final)