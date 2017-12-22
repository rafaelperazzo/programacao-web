# -*- coding: utf-8 -*-
import numpy as np

n = int (input('Digite a quant de linhas: '))
m = int(input('Digite a quant de colunas: '))

a = np.zeros ((n,m))

for i in range (0, n, 1):
    for j in range (0, m, 1):
        a[i,j] = float (input('Digite os elementos: '))

soma = 0
cont = 0

for i in range (0, n, 1):
    for j in range (0,m,1):
        soma = soma + a[i,j]
        print (soma)
    if soma - a[i,i] < a[i,i]:
        cont = cont + 1
    soma = 0
            
if cont == n:
    print ('SIM')
else:
    print ('NAO')

    
            
        
        
    
