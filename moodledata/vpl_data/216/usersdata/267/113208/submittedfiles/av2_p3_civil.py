# -*- coding: utf-8 -*-
import numpy as np
n=int(input('Dimensão do tabuleiro: '))
print()
a=np.zeros((n,n))
x=int(input('Número da linha em que a torre se encontra: '))
if x>n:
    while x>n:
        x=int(input('VALOR INVÁLIDO. Número da linha em que a torre se encontra: '))
print()
y=int(input('Número da coluna em que a torre se encontra: '))
if y>n:
    while y>n:
        y=int(input('VALOR INVÁLIDO. Número da coluna em que a torre se encontra: '))
print()
for i in range(0,n,1):
    for j in range(0,n,1):
        a[i,j]=int(input('Digite o valor da posição %d%d: '%(i+1,j+1)))
somaL=0
for i in range(0,n,1):
    somaL=somaL+a[x-1,i]
somaC=0
for i in range(0,n,1):
    somaC=somaC+a[i,y-1]
peso=somaL+somaC-a[x-1,y-1]
print(peso)