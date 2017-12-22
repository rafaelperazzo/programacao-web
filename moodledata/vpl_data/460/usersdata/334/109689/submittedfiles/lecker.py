# -*- coding: utf-8 -*-
n = int(input())

a = []
for i in range(n):
    a.append(int(input()))

c = 0    
for i in range(n):
    if a[i]==a[n-1] and a[i]<a[i-1]:
        c += 1
    elif a[i]==a[0] and a[i]<a[i+1]:
        c += 1
    else:
        if a[i]>a[i+1] and a[i]>a[i-1]:
            c += 1
    
b = []
for i in range(n):
    b.append(int(input()))

d = 0    
for i in range(n):
    if b[i]==b[n-1] and b[i]<b[i-1]:
        d += 1
    elif b[i]==b[0] and b[i]<b[i+1]:
        d += 1
    else:
        if b[i]>b[i+1] and b[i]>b[i-1]:
            d += 1

if c==1:
    print('S')
else:
    print('N')

if d==1:
    print('S')
else:
    print('N')