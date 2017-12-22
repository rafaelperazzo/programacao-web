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
