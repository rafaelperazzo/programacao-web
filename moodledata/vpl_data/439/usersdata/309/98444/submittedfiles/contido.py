# -*- coding: utf-8 -*-

na=int(input("Digite a quantidade de elementos de A:"))
nb=int(input("Digite a quantidade de elementos de B:"))

a=[]
b=[]

for i in range (0, na, 1):
    a.append(int(input("Digite o %dº elemento de A:" %(na+1))))

for i in range (0, nb, 1):
    a.append(int(input("Digite o %dº elemento de B:" %(nb+1))))   