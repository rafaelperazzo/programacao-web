# -*- coding: utf-8 -*-
import numpy as np

m=int(input("Insira m: "))
while m<2 or m>1000:
    m=int(input("Insira m: "))
    
n=int(input("Insira n: "))
while n<2 or n>1000:
    n=int(input("Insira n: "))

quadra=np.empty([m,n])
transq=np.empty([n,m])

for i in range(0,m,1):
    for j in range(0,n,1):
        quadra[i][j]=int(input("Digite um valor: "))

for i in range(0,n,1):
    for j in range(0,m,1):
        transq[i][j]=quadra[j][i]

valor=0
for i in range(0,n-1,1):
    if sum(transq[i]) <= sum(transq[i+1]):
        valor=sum(transq[i])
    else:
        valor=sum(transq[i+1])

    