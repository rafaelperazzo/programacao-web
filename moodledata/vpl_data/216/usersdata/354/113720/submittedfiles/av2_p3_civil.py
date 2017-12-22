# -*- coding: utf-8 -*-


ordem=int(input('digite a dimensao n da matriz: '))
x=int(input('digite a linha do numero: '))
y=int(input('digite a coluna do numero: '))
matriz=np.zeros((ordem,ordem))
for i in range(0,ordem,1):
    matriz[i,j]=int(input('digite os valores da matriz: '))

i=x
soma=0
for j in range (0,ordem,1):
    if i!=x:
        soma1=soma1+matriz[i,j]
        
peso=soma+soma1
print(peso)