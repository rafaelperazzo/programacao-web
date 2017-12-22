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
c11=0
for i in range(0,n-1,1):
    if b[i]<b[i+1]:
        continue
    else:
        c11=c11+1
c22=0
for i in range(0,n-1,1):
    if b[i]>b[i+1]:
        continue
    else:
        c22=c22+1
c111=0
for i in range(0,n-1,1):
    if c[i]<c[i+1]:
        continue
    else:
        c111=c111+1
c222=0
for i in range(0,n-1,1):
    if c[i]>c[i+1]:
        continue
    else:
        c222=c222+1
if c1==0:
    print("S")
else:
    print("N")
if c11==0:
    print("S")
else:
    print("N")
if c111==0:
    print("S")
else:
    print("N")
if c2==0:
    print("S")
else:
    print("N")
if c22==0:
    print("S")
else:
    print("N")
if c222==0:
    print("S")
else:
    print("N")
if c1!=0 and c2!=0:
    print("S")
else:
    print("N")
if c11!=0 and c22!=0:
    print("S")
else:
    print("N")
if c111!=0 and c222!=0:
    print("S")
else:
    print("N")
        