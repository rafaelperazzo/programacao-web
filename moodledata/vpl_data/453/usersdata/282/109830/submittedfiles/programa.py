# -*- coding: utf-8 -*-
import numpy as np
m=[]
n=int(input('Digite a ordem da matriz: '))
while not n>=3:
    n=int(input('Digite a ordem da matriz: '))
for i in range (0,n,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(int(input('Digite o valor da linha/coluna: ')))
    m.append(linha)
ntrans=np.empty([n,n])
for i in range(0,n,1):
    for j in range (0,n,1):
        ntrans[j][i]=m[i][j]
        
somatotal = sum(m[0]) + sum(ntrans[0]) - 2*(m[0][0])
for i in range(0,n,1):
    for j in range(0,n,1):
        if somatotal > sum(m[i]) + sum (ntrans[j]) - 2*(m[i][j]):
            somatotal=somatotal
        else:
            somatotal=sum(m[i])+sum(ntrans[j])-2*(m[i][j])
            
print(int(somatotal))

