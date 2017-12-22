# -*- coding: utf-8 -*-
import numpy as np

n=int(input("Digite n: "))
while n < 3:
    n=int(input("Digite n: "))

tab=np.empty([n,n])
trans=np.empty([n,n])

for i in range (0,n,1):
    for j in range (0,n,1):
        tab[i][j]=int(input("Digite um valor: "))

for i in range (0,n,1):
    for j in range (0,n,1):
        trans[i][j]=tab[j][i]

print(tab)
print(trans)

peso=(sum(tab[0]))+(sum(trans[0]))-(2*(tab[0][0]))
print(peso)

for i in range (0,n-1,1):
    for j in range (0,n-1,1):
        if peso >= (sum(tab[i+1]))+(sum(trans[j+1]))-(2*tab[i+1][j+1]):
            peso=peso
        else:
            peso = (sum(tab[i+1]))+(sum(trans[j+1]))-(2*(tab[i+1][j+1]))

print(peso)