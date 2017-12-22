# -*- coding: utf-8 -*-

n= int (input('Digite a quantidade de termos da primeira lista: '))
m= int (input('Digite a quantidade de termos da segunda lista: '))

a = []
b = []

for i in range (0,n,1):
    valor_a = float (input('Digite o elemento da primeira lista: '))
    a.append (valor_a)

for i in range (0,m,1):
    valor_b = float (input('Digite o elemento da segunda lista: '))
    b.append (valor_b)

k = 0
cont = 0
if n>m:
    for k in range (0,n,1):
        for i in range (0,n,1):
            if a[k] == b[i]:
                cont = cont + 1
j = 0
if m>n:
    for j in range (0,m,1):
        for i in range (0,m,1):
            if b[k] == a[i]:
                cont = cont + 1
    
print (cont)