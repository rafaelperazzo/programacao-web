# -*- coding: utf-8 -*-
n=int(input("Insira n: "))
a=[]
for i in range (0,n,1):
    a.append(int(input("Digite o valor %d: " %(i+1))))
imp=[]
par=[]
for i in range (0,n,1):
    if a[i]%2 == 0:
        par.append(a[i])
    else:
        imp.append(a[i])
print(sum(imp))
print(sum(par))
print(len(imp))
print(len(par))
print(a)
