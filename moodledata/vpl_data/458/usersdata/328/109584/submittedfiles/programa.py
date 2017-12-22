# -*- coding: utf-8 -*-
n=int(input("Digite a dimensão do tabuleiro:"))
t=[]
for i in range (n):
    l=[]
    for j in range (n):
        l.append(float(input('Adicione pesos:')))
    t.append(l)
print (t)

