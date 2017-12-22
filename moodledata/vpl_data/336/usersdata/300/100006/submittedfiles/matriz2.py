# -*- coding: utf-8 -*-
import numpy as np
cont1=0
cont2=0
cont3=0
dim=int(input('Digite a dimensão da matriz: '))
while dim<2:
    dim=int(input('Digite a dimensão da matriz: '))
matriz=np.empty([dim,dim])
matriztrans=np.empty([dim,dim])
matrizdiag=np.empty([2,dim])
matrizultprim=np.empty([dim,dim])

for i in range(0,dim,1):
    for j in range(0,dim,1):
        matriz[i][j]=float(input('Digite o valor na linha %d e na coluna %d: ' %((i+1),(j+1))))
        
for i in range(0,dim,1):
    for j in range(0,dim,1):
        matriztrans[i][j]=matriz[j][i]

for i in range(0,dim,1):
    for j in range(0,dim,1):
        matrizultprim[i][j] = matriz[i][dim-1-j]

for i in range(0,dim,1):
    matrizdiag[0][i]=matriz[i][i]
for i in range(0,dim,1):
    matrizdiag[1][i]=matrizultprim[i][i]
    
for i in range(0,dim-1,1):
    if sum(matriz[i]) == sum(matriz[i+1]):
        cont1 = cont1 + 1   
    
for i in range(0,dim-1,1):
    if sum(matriztrans[i]) == sum(matriztrans[i+1]):
        cont2 = cont2 + 1
        
if sum(matrizdiag[0]) == sum(matrizdiag[1]):
    cont3 = cont3 + 1
    
if cont3 == dim-1 and cont2 == dim+1 and cont3 == 1:
    print('S')
else:
    print('N')
