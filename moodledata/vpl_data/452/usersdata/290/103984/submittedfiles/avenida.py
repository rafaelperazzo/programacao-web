# -*- coding: utf-8 -*-
m=int(input("Digite a quantidade de quadras no sentido norte sul: "))
n=int(input("Digite a quantidade de quadras no sentido leste oeste: "))
a=[]
for i in range(0,m,1):
    l=[]
    for j in range(0,n,1):
        l.append(int(input("Digite o valor: ")))
    a.append(l)
s=0
k=0
c=0
for i in range(0,n,1):
    for j in range(0,m-1,1):
        s=s+a[i][j]
        k=k+a[i][j+1]
    if s<k:
        c=s
    else:
        c=k
print(c)
        