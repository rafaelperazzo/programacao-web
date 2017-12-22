# -*- coding: utf-8 -*-

import numpy as np
soma=0
pesos=[]
n=int(input('Digite a dimensão do tabuleiro(n>=3): '))

a=np.zeros((n,n))
for i in range(0,n,1):
  for j in range(0,n,1):
    a[i,j] = int(input('Digite o elemento da matriz: '))


 

somalinha = 0
somacoluna = 0

for i in range(0,n,1):
  for e in range (0,n,1):
    for j in range(0,n,1):
      somalinha= somalinha + a[i,j]
      somacoluna = somacoluna + a[j,e]
    soma = somalinha + somacoluna - 2*a[i,e]
      
    pesos.append(soma)
    somalinha = 0
    somacoluna = 0
    soma = 0
      
print ((max(pesos)))