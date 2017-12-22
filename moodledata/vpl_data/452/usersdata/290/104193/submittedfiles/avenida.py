# -*- coding: utf-8 -*-
m=int(input("Digite a quantidade de quadras no sentido norte sul: "))
while m<2 or m>1000:
    m=int(input("Digite a quantidade de quadras no sentido norte sul: "))
n=int(input("Digite a quantidade de quadras no sentido leste oeste: "))
while n<2 or n>1000:
    n=int(input("Digite a quantidade de quadras no sentido leste oeste: "))
a=[]
for i in range(0,m,1):
    l=[]
    for j in range(0,n,1):
        l.append(int(input("Digite o valor: ")))
    a.append(l)
    
s=0
k=0
c=[]
for j in range(0,n-1,1):
    s=0
    k=0
    for i in range(0,m,1):
        s=s+a[i][j]
        k=k+a[i][j+1]
    if s<k:
        c.append(s)
    else:
        c.append(k)
d=0
for i in range(0,len(c)-1,1):
    if c[i]<c[i+1]:
        d=c[i]
    else:
        d=c[i+1]
print(d)
        