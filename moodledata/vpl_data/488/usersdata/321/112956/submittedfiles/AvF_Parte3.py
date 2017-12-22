# -*- coding: utf-8 -*-
n= int(input('Valor de n: '))
a= []

for i in range(n):
    a.append(int(input('Valor%d: ' % i)))
    par=[]
    impar= []
    while i>=n:
        if i%2==0:
            par.append(i)
        elif i%2!=0:
            impar.append(i)













print(a)
print(par)
print(impar)