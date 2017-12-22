# -*- coding: utf-8 -*-
n=int(input('digite quantos valos a lista comporta: '))
a=[]
for i in range (0,n,1):
    a.append(int(input('digite um elemento a lista: ')))
imp=[]
par=[]
for i in range (0,n,1):
    if a[i]%2==0 :
        par.append(a[i])
    else :
        imp.append(a[i])
print(sum(imp))
print(sum(par))
print(len(imp))
print(len(par))
print(a)
