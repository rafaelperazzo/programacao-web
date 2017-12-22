# -*- coding: utf-8 -*-
n = int(input('Valor: '))
l1 = []
l2 = []
for i in range (0,n,1):
    l1.append(int(input('Valor: ')))
for i in range (0,n,1):
    l2.append(int(input('Valor: ')))
c1=0
for i in range (1,n,1):
    if l1[i] > l1[i-1] and l1[i] > l1[i+1]:
        c1 = c1 + 1
if l1[0]>l1[i]:
    c1 = c1 + 1
if l1[n-1] > l1[n-2]:
    c1 = c1 + 1
c2=0
for i in range (1,n,1):
    if l2[i] > l2[i-1] and l2[i] > l2[i+1]:
        c2 = c2 + 1
if l2[0]>l2[i]:
    c2 = c2 + 1
if l1[n-1] > l1[n-2]:
    c2 = c2 + 1
if c1==1 and c2==1:
    print('S')
    print('S')
elif c1==1 and c2!=1:
    print('S')
    print('N')
elif c1!=1 and c2++1:
    print('N')
    print('S')
else: 
    print('N')
    print('N')