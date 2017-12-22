# -*- coding: utf-8 -*-
n=100000
l=[]
for i in range (n):
    v=[]
    for j in range (n):
        v.append(int(input('Digite o Valor desejado:')))
    l.append(v)
soma=sum(l[0])
print(soma)

    