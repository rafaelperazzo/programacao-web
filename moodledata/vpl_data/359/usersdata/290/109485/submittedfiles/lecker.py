# -*- coding: utf-8 -*-
n=int(input("Digite o valor de n: "))
l=[]
m=[]
for i in range(0,n,1):
    l.append(int(input("Digite o valor: ")))
for i in range(0,n,1:
    m.append(int(input("Digite o valor: ")))
c=0
for i in range(0,n-2,1):
    if l[i]<l[i+1]>l[i+2]:
        c=c+1
if l[0]>l[1] or l[n-1]>l[n-2]:
    c=c+1
if c==1:
    print("S")
else:
    print("N")

d=0
for i in range(0,n-2,1):
    if m[i]<m[i+1]>m[i+2]:
        d=d+1
if m[0]>m[1] or m[n-1]>m[n-2]:
    d=d+1
if d==1:
    print("S")
else:
    print("N")
