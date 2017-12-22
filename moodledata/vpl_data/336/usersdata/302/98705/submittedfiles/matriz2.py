# -*- coding: utf-8 -*-
import numpy as np
cont1 = 0
cont2 = 0
cont3 = 0
n = int(input('Digite a dimensão da matriz quadrada: '))
while(n<2):
    n = int(input('Digite a dimensão da matriz quadrada: '))
matriz = np.empty([n,n])
matriztrans = np.empty([n,n])
matrizdiag = np.empty([2,n])
matrizultprim = np.empty([n,n])
for i in range(n):
    for j in range(n):
        matriz[i][j] = float(input('Digite o valor na linha %d e na coluna %d: '%((i+1),(j+1))))
#Trans
for i in range(n):
    for j in range(n):
        matriztrans[i][j] = matriz[j][i]

for i in range(n):
    for j in range(n):
        matrizultprim[i][j] = matriz[i][n-1-j]
#diag
for i in range(n):
    matrizdiag[0][i] = matriz[i][i]
for i in range(n):
    matrizdiag[1][i] = matrizultprim[i][i]

#cont
for i in range(n-1):
    if sum(matriz[i]) == sum(matriz[i-1]):
        cont1 = cont1+1
for i in range(n-1):
    if sum(matriztrans[i]) == sum(matriztrans[i-1]):
        cont2 = cont2 + 2
if sum(matrizdiag[0]) == sum(matrizdiag[1]):
    cont3 = cont3 + 1

if cont1 == n-1 and cont2 == n-1 and cont3 ==1:
    print('S')
else:
    print('N')
 
        
