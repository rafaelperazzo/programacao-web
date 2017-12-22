# -*- coding: utf-8 -*-

n= int (input('Digite a quantidade de termos da primeira lista: '))
m= int (input('Digite a quantidade de termos da segunda lista: '))

n = []
m = []

for i in range (0,n,1):
    valor_n = float (input('Digite o elemento da primeira lista: '))
    n.append (valor_n)

for i in range (0,m,1):
    valor_m = float (input('Digite o elemento da segunda lista: '))
    m.append (valor_m)

k = 0
cont = 0
if n>m:
    for i in range (0,n,1):
        if n[k] == m[i]:
        cont = cont + 1
    k = k + 1

if m>n:
    for i in range (0,m,1):
        if m[k] == n[i]:
        cont = cont + 1
    k = k + 1
    
print (cont)