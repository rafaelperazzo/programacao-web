# -*- coding: utf-8 -*-
import numpy as np

m=int(input("Digite m: "))
while m<=2 or m>=1000:
    m=int(input("Digite m: "))

n=int(input("Digite n: "))
while n<=2 or n>=1000:
    n=int(input("Digite n: "))

matriz=np.empty([m,n])


for i in range(0,m,1):
    for j in range(0,n,1):
        matriz[i][j]=int(input("Digite um valor: "))

min=0
for i in range(0,m-1,1):
    if sum(matriz[i]) <= sum(matriz[i+1]):
        min=int(sum(matriz[i]))
    else:
        min=int(sum(matriz[i+1]))

print(min)