# -*- coding: utf-8 -*-
import numpy as np
cont1=0
cont2=0
cont3=0
dim=int(imput("Dimensão n da matriz: "))
while dim < 2:
    dim=int(imput("Dimensão n da matriz: "))
matriz=np.empty([dim,dim])
matriztrans=np.empty([dim,dim])
matrizdiag=np.empty([2,dim])
matrizultprim=np.empty([dim,dim])

for i in range(0,dim,1):
    for j in range(0,dim,1):
        matriz[i][j]=float(imput("Digite o valor na linha" + i+1 + " e coluna" + j+1 )
