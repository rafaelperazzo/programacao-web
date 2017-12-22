# -*- coding: utf-8 -*-
ordem=int(input('Digite a dimensao n da matriz: '))
x=int(input('Digite a linha do numero: '))
y=int(input('Digite o valor da coluna: '))
matriz=np.zeros((ordem,ordem))
for i in range(0,ordem,1):
    for j in range(0,ordem,1):
        matriz[i,j]=int(input('Digite os valores para a matriz: '))
        
i=x
soma=0
for j in range (0,ordem,1):
    if j!= y:
        soma=soma+matriz[i,j]
        
j=y
soma1=0
for i in range (0,ordem,1):
    if i!= y:
        soma1=soma1+matriz[i,j]

peso=soma+soma1
print(peso)



peso= soma+soma1
print(peso)



