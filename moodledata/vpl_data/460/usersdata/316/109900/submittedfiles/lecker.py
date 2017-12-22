# -*- coding: utf-8 -*-
def lecker(a,b,c):
    if a<b and b>c:
        return true
a=[]
b=[]
ct=0
ctb=0
n=int(input('digite a quantidade de elemento da lista: '))
for i in range(0,n,1):
    vl_a=float(input('digite um numero: '))
    a.append(vl_a)
for i in range(0,n,1):
    vl_b=float(input('digite um numero: '))
    b.append(vl_b)
for i in range(0,n,1):
    if i==0:
        if a[i]>a[i+1]:
            ct=ct+1
        elif i==n-1:
            if a[n-1]>a[n-2]:
                ct=ct+1
        else:
            if lecker(a[i-1],a[i],a[i+1]):
                ct=ct+1
if ct==1:
    print('S')
else:
    print('N')
for i in range(0,n,1):
    if i==0:
        if b[i]>b[i+1]:
            ctb=ctb+1
        elif i==n-1:
            if b[n-1]>b[n-2]:
                ctb=ctb+1
        else: if lecker(b[i-1],b[i],b[i+1]):
            ctb=ctb+1
if ctb==1:
    print('S')
else:
    print('N')