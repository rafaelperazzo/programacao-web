# -*- coding: utf-8 -*-


n=0
while n<3:
    n=int(input('Digite a dimensão da matriz: '))


linha=[]
coluna=[]
for i in range(0,n,1):
    soma=0
    for j in range(0,n,1):
        soma=soma+a[i,j]
    linha.append(soma)
    soma=0
    for j in range(0,n,1):
        soma=soma+a[j,i]
    coluna.append(soma)
if 