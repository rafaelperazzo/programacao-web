# -*- coding: utf-8 -*-
n=int(input('digite a quantidade de salas:'))
a=[]
for i in range(1,n+1,1):
    a.append(int(input('quantidade de vidas:')))
x=int(input('porta de entrada:'))
y=int(input('porta de saida:'))
soma=0
for i in range(x,y+1,1):
    soma=soma+a[i]
print(soma)

    

