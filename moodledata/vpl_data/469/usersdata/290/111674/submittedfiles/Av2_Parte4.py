# -*- coding: utf-8 -*-
m=int(input("Digite a quantidade de ruas n-s: "))
n=int(input("Digite a quantidade de quadras no sentido l-o: "))
matriz=[]
for i in range(0,m,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(int(input("Digite o valor da quadra: ")))
    matriz.append(linha)
valor=[]
for i in range(0,m,1):
    valor.append(sum(matriz[i]))
maior=101
for i in range(0,m,1):
    if valor[i]<maior:
        maior=valor[i]
