# -*- coding: utf-8 -*-
n = int(input('Digite a quantidade de valores: '))
lista = []
a = 0
b = 0
c = 0
d = 0
for i in range (0,n,1):
    lista.append(int(input('Digite o valor de n: ')))
for i in range (0,n,1):
    if lista[i]%2 == 0:
        a = a + lista[i]
        b = b + 1
    else:
        c = c + lista[i]
        d = d + 1
        
print(c)
print(a)
print(d)
print(b)
print(lista)


