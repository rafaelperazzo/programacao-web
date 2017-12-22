# -*- coding: utf-8 -*-
import numpy as np
cont1=0
cont2=0
cont3=0
dim=int(input("dimensão n da matriz: "))

while dim<2:
    dim=int(input("dimensao n da matriz: "))
matriz=np.empty([dim,dim])
matriztrans=np.empty([dim,dim])
matrizdiag=np.empty([2,dim])
matrizultprim=np.empty([dim,dim])

for i in range(0,dim,1):
    for j in range(0,dim1):
        matriz[i][j]=float(input("digite o valor na linha %d e na coluna %d: " %((i+1),(j+1))))
        
#trans
for i in range (0,dim,1):
    for j in range (0,dim,1):
        matriztrans[i][j]=matriz[j][i]
        



