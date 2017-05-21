# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
k = int(input('Digite o valor de k: '))
soma = 0
termo=0
for i in range(0,k+1,1):
    termo =((-1**i)*(4/((2*i)+1)))
    soma = soma+termo
print(soma)    
