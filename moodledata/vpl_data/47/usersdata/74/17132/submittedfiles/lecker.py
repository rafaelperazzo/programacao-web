# -*- coding: utf-8 -*-
from __future__ import division

n = input('Digite o tamanho do vetor: ')

i = 1
k = 1
a = []
b = []

while n>=i:
    a.append(input('Digite os valores do vetor a: '))
    i = i+1
while n>=k:
    b.append(input('Digite os valores do vetor b: '))
    k = k+1
    
j = 1
l = 1
conta = 0
contb = 0
m = n-1

while m>j:
    if a[j]>a[j-1] and a[j]>a[j+1]:
        conta = conta+1
    j = j+1
while m>l:
    if b[l]>b[l-1] and b[l]>b[l+1]:
        contb = contb+1
    l = l+1
if conta == 1:
    print('S')
else:
    print('N')
    
if contb == 1:
    print('S')
else:
    print('N')