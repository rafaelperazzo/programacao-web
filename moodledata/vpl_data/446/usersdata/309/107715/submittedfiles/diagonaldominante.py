# -*- coding: utf-8 -*-
m=[]
n=int(input())
for i in range (n):
    lista=[]
    for j in range (n):
      lista.append(int(input('Digite um elemento:')))
    m.append(lista)
        
for i in range(n):
     m[i][i]

