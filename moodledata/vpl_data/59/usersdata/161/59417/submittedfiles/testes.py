import numpy as np
linhas=int(input('Informe o número de linhas da matriz:'))
colunas=int(input('Informe o número de colunas da matriz:'))
a=np.zeros((linhas,colunas))
b=np.zeros((linhas,colunas))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('Digite o elemento:'))
for i in range(0,b.shape[0],1):
    for j in range(0,b.shape[1],1):
        b[i,j]=a[j,i]
print(b)    
