# -*- coding: utf-8 -*-
n=int(input('digite o valor da quantidade de degraus:'))
a=[]
for i in range(1,n+1,1):
    a.append(int(input('degraus:')))
b=[]
for i in range (0,n-1,1):
    b.append(a[i]-a[i+1])
for i in range (0,len(b),1):
    if (b[i]<0):
        b[i]=b[i]*(-1)
    
print(b)
















def degrau (c, d):
    for i in range (0, n-1, 1):
        c.append(c(i)-c(i-1))
    for i in range (0, len(d), 1):
        if (d(i)<0):
            d(i)=d(i)*(-1)
    return(d)
    
n=int(input('digite a quantidades de elementos:'))
c=[]
d=[]
for i in range (0, n, 1):
    valor=int(input('valor da lista:'))
    c.append(valor)
print(degrau(c,b))