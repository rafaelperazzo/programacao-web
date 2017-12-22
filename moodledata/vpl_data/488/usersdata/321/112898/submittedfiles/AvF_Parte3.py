# -*- coding: utf-8 -*-
n= int(input('Valor de n: '))
a= []

for i in range(n):
    a.append(int(input('Valor%d: ' % i)))
    par=[]
    impar= []
    for j in range (n):
        if i%2==0:
            par.append(i)
            i+=1
        else:
            impar.append(i)
            i+=1
print(a)
print(par)
print(impar)