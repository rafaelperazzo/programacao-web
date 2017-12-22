# -*- coding: utf-8 -*-
n = int(input('Digite a ordem n da matriz n x n: '))

matriz=[]
for i in range (0, n, 1):
    linha=[]
    for i in range (0, n, 1):
        linha.append(int(input('Digite um elemento da matriz: ')))
    matriz.append(linha)
    
lista_somas=[]

for i in range (0, n, 1):
    s=sum(matriz[i])
    lista_somas.append(s)
    
for i in range (0, n, 1):
    scol=0
    for j in range (0, n, 1):
        scol+=matriz[j][i]
    lista_somas.append(scol)
    
contador=0
for i in range (0, len(lista_somas)-1, 1):
    if lista[i]==lista[i+1]:
        contador+=0
    if not lista[i]==lista[i+1]:
        contador+=1

if contador==0:
    print('S')
if not contador==0:
    print('N')
        
        

