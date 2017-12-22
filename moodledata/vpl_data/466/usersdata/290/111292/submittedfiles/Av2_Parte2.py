# -*- coding: utf-8 -*-
n=int(input("Digite a quantidade de elementos das listas: "))
a=[]
for i in range(0,n,1):
    a.append(int(input("Digite o valor para a: ")))
b=[]
for i in range(0,n,1):
    b.append(int(input("Digite o valor para b: ")))
c=[]
for i in range(0,n,1):
    c.append(int(input("Digite o valor para c: ")))
c1=0
for i in range(0,n-1,1):
    if a[i]<a[i+1]:
        continue
    else:
        c1=c1+1
c2=0
for i in range(0,n-1,1):
    if a[i]>a[i+1]:
        continue
    else:
        c2=c2+1
if c1==0:
    print("S")
else:
    print("N")
if c2==0:
    print("S")
else:
    print("N")
if c1!=0 and c2!=0:
    print("S")
else:
    print("N")
        