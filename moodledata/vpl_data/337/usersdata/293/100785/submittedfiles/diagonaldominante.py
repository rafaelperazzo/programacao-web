# -*- coding: utf-8 -*-
n=int(input("Digite a ordem da matriz: "))

while(True):
    if n<2:
        n=int(input("Digite a ordem da matriz: "))
    else:
        break
matriz=[]    
for i in range(0,n,1):
    matriz_linha=0
    for j in range(0,n,1):
        matriz_linha.append(input("Digite o elemento (%d,%d): "%(i+1,j+1)))
    matriz.append(matriz_linha)
print(matriz)
