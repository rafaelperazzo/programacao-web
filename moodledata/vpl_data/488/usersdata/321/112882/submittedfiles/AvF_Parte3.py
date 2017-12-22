# -*- coding: utf-8 -*-
n= int(input('Valor de n: '))
a= []

for i in range(n):
    a.append(int(input('Valor%d: ' % i)))
for i in range (a):
    if i%2==0:
        par.append(i)
    else:
        impar.append(i)
print(a)
print(par)
print(impar)