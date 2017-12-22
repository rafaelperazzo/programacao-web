# -*- coding: utf-8 -*-
import numpy as np

m=int(input("Digite a quantidade de linhas:"))
n=int(input("Digite a quantidade de colunas:"))
matri=np.empty([m, n])
for i in range (m-1, -1, -1):
  for j in range (n-1, -1, -1):
    matri[i][j]=(int(input("Digite um elemento para a matriz:")))



print(matri)

