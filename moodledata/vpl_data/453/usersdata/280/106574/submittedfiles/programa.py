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

peso=(sum(tab[0]))+(sum(trans[0]))-(2*(tab[0][0]))


for i in range (0,n,1):
    for j in range (0,n,1):
        if peso >= (sum(tab[i]))+(sum(trans[j]))-(2*tab[i][j]):
            peso=peso
        else:
            peso=(sum(tab[i]))+(sum(trans[j]))-(2*(tab[i][j]))

print(int(peso))