# -*- coding: utf-8 -*-
M= int(input('Número de quadras no sentido Norte-Sul: '))   #linhas
while M<=2 and M>=1000:
    print('Valor inválido! Insira um valor válido (2-1000): ')

N= int(input('Número de quadras no sentido Leste-Oeste: '))   #colunas
while M<=2 and M>=1000:
    print('Valor inválido! Insira um valor válido (2-1000): ')

matriz=[]
for i in range (0,M,1):
    linha=[]
    for j in range (0,N,1):
        linha.append(input('Digite um valor: '))
    matriz.append(linha)