# -*- coding: utf-8 -*-
n = int(input())

a = []
for i in range(n):
    a.append(int(input()))

c = 0    
for i in rage(n):
    if a[i]>a[i+1] and a[i]>a[i-1]:
        c += 1
    
b = []
for i in range(n):
    b.append(int(input()))

d = 0    
for i in rage(n):
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