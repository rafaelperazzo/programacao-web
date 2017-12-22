 -*- coding: utf-8 -*-
v=int(input('Digite o volume inicial da TV: '))
t=int(input('Digite o número de trocas de volume: '))
a=[]

for i in range (0,t,1):
    a.append(int(input('Digite a modificação de volume: ')))

M=100
m=0
soma=v
for j in range (0,len(a),1):
    soma=soma+a[j]
    if (soma>M):
        soma=M
    elif (soma<m):
        soma=m
    else:
        soma=soma+0
print(soma)
    
 