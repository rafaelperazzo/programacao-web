# -*- coding: utf-8 -*-
n=int(input("Digite o valor de n: "))
l=[]
for i in range(0,n,1):
    l.append(int(input("Digite o valor: ")))
c=0
for i in range(0,n-2,1):
    if l[i]<l[i+1]>[i+2]:
        c=c+1
if l[0]>l[1] or l[n]>l[n-1]:
    c=c+1
if c==1:
    print("S")
else:
    print("N")
    
