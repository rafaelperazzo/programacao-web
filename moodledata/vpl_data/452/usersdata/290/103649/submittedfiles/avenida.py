# -*- coding: utf-8 -*-
m=int(input("Digite a quantidade de quadras no sentido norte sul: "))
n=int(input("Digite a quantidade de quadras no sentido leste oeste: "))
a=[]
for i in range(0,n,1):
    l=[]
    for j in range(0,m,1):
        l.append(int(input("Digite o valor: ")))
    a.append(l)
print(a)