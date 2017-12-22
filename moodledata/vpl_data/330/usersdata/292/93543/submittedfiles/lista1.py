# -*- coding: utf-8 -*-
import os
n = int(input("Digite o número de itens da lista: "))
os.system("clear")
k, somat_i, somat_p, cont_i, cont_p = [], 0, 0, 0, 0

for i in range(1,n+1):
    k.append(int(input("Digite o %dº valor: "%i)))
    
for i in k:
    if i%2 == 0:
        somat_p += i
        cont_p += 1
        
    else:
        somat_i += i
        cont_i += 1

os.system("clear")

print(somat_i)
del somat_i

print(somat_p)
del somat_p

print(cont_i)
del cont_i

print(cont_p)
del cont_p

print(k)
del k