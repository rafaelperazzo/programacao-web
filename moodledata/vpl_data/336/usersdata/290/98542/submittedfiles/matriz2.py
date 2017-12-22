# -*- coding: utf-8 -*-
n=int(input("Digite um valor >=2: "))
while n<2:
    n=int(input("Digite um valor >=2: "))
a=[]
for i in range(0,n,1):
    b=[]
    for i in range(0,n,1):
        b.append(int(input("Digite os valores da matrize:")))
    a.append(b)
c=0
d=0
for i in range(0,n,1):
    c=c+a[i][i]
    d=a+a[i][n-i]
for i in range(0,n,1):
    if c==d==sum(a[i]):
        print("S")
    else:
        print("N")