from __future__ import division
import numpy as np
linhas = input ('Digite a quantidade de linhas:')
colunas = input ('Digite a quantidade de colunas:')
a =np.zeros((linhas,colunas))

print (a)

for i in range (0, a.shape[0], 1):
    for j in range (0,a.shape[1],1):
        a[i,j]=input('Digite o elemento %d%d'%(i,j))

print (a)

cont = 0
meio = colunas//2
y = colunas -1
for x in range (0,linhas,1):
    if a[:,x]!=a[:,y]:
        cont = cont+1
        y = y-1

if cont == 0:
    print ('É simétrica')
else:
    print ('Não é simétrica')