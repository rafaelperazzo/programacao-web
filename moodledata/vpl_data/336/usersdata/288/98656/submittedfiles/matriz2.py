# -*- coding: utf-8 -*-
import numpy as np
cont1=0
cont2=0
cont3=0
dim=int(input('Digite um valor >=2: '))
while n<2:
    n=int(input('Digite um valor >=2: '))
matriz=np.empy([dim,dim])
matriztrans=np.empy([2,dim])
matrizultprim=np.empy([dim,dim])
mareizdiag=np.empy([dim,dim])


for i in range (0,dim,1):
    for j in range (0,dim,1):
        matriz[i][j]=float(input('Digite um valor'))
    
for i in range (0,dim,1):
    for j in range (0,dim,1):
        matriztrans[i][i]=matriz[j][i]

for i in range (0,dim,1):
    for j in range (0,dim,1):
        matrizultprim[i][j]=matriz[i][dim-1-j]

for i in range (0,dim,1):
    matrizdiag[0][i]=matriz[i][i]
for i in range (0,dim,1):
    matrizdiag[i][i]=matrizultprim[i][i]

for i in range (0,dim,1):
    if sum(matriz[i])==sum(matriz[i+1]):
        cont1+=1
for i in range (0,dim-1,1):
    if sum(matriztrans[i])==sum(matriz[i+1]):
        cont2+=1
if sum(matrizdiag[0])==sum(matrizdiag[1]):
    cont3+=1
    
    
if cont1==dim-1 and cont2==dim-1 and cont3==1:
    print ('S')
else:
    print ('N')
    
    
            




    
