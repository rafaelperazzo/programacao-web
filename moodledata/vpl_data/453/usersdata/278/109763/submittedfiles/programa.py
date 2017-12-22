# -*- coding: utf-8 -*-
N = int(input('Digite a dimensão do tabuleiro quadrado: '))
while (N<3):
    N = int(input('Digite a dimensão (N>=3) do tabuleiro quadrado: '))
m=[]
for i in range (0,N,1):
    lista=[]
    for j in range (0,N,1):
        lista.append(int(input('Digite o número da linha%.d e coluna%.d: ' %(i,j))))
    m.append(lista)
lista_L=[]
for i in range (0,N,1):
    soma_L=0
    for j in range (0,N,1):
        soma_L+=m[i][j]
    lista_L.append(soma_L)
print(lista_L)
lista_C=[]
for j in range (0,N,1):
    soma_C=0
    for i in range (0,N,1):
        soma_C+=m[i][j]
    lista_C.append(soma_C)
print(lista_C)
lista_f=[]
for i in range (0,N,1):
    for j in range (0,N,1):
        lista_f.append(lista_L[i]+lista_C[j]-m[i][j])
print(lista_f)
maior=0
for i in range (0,N,1):
    if lista_f[i]>maior:
        maior=lista_f[i]
print(maior)