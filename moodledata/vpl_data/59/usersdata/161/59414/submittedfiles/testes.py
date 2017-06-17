import numpy as np
linhas=int(input('Informe o número de linhas da matriz:'))
colunas=int(input('Informe o número de colunas da matriz:'))
a=np.zeros((m,m))
b=np.zeros((m,m))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('Digite o elemento:'))
for i in range(0,b.shape[1],1):
    b[i,j]=a[j,i]
print(b)    
