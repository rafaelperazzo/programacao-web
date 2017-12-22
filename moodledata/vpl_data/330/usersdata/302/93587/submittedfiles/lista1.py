# -*- coding: utf-8 -*-
n = int(input('Digite a quantidade de valores da matriz: '))
a = []
par = []
impar = []
for i in range(0,n,1):
    a.append(int(input('Digite a%d:' %(i+1))))
s = 0
j = 0
for i in range(0,n,1):
    if a[i]%2 != 0:
        s = s + a[i]
        par.append(a[i])
print(s)
for i in range(0,n,1):
    if a[i]%2 == 0:
        j = j + a[i]
        impar.append(a[i])
print(j)
print(len(impar))
print(len(par))
print(a)


    
    




