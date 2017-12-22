# -*- coding: utf-8 -*-
import numpy as np

n = int (input ('Digite a dimensão do quadrado mágico: '))

while n<3:
    n = int (input('Digite a dimensão do quadrado mágico: '))

matriz = np.zeros ((n,n))
for i in range (0,n,1):
    for j in range (0,n,1):
        matriz[i,j] = int (input ('Digite os elementos do quadrado mágico: '))

somalinha = 0
soamcoluna = 0

a = []
b = []

for i in range (0,a.shape[0],1):
  for j in range (0,a.shape[1],1):
    somalinha = somalinha + a[i,j]
  a.append (somalinha)
  somalinha = 0

print (somalinha)

for j in range (0,a.shape[1],1):
  for i in range (0,a.shape[0],1):
    somacoluna = somacoluna + a[i,j]
  b.append (somacoluna)
  somacoluna = 0   

print (somacoluna)

'''
for i in range (0,len(somalinha),1):
  if i == 0:
    if a[i] == a[i+1]:
      cont = cont + 1
  if i == len (somalinha):
    if a[i] == a[i+1]:
      cont = cont + 1
'''