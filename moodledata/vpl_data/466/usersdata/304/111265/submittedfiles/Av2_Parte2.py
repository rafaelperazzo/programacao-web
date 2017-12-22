# -*- coding: utf-8 -*-
n = int(input('Digite n:' ))
lista1 = []
lista2 = []
lista3 = []
for i in range (0,n):
    lista1.append(int(input('Digite n: ')))
for i in range (0,n):
    lista2.append(int(input('Digite n: ')))
for i in range (0,n):
    lista3.append(int(input('Digite n: ')))
    
c1 = 0
d1 = 0
s1 = 0

for i in range (0,(len(lista1)-1),1):
    if lista1[i] < lista1[i+1]:
        c1 = 1
    elif lista1[i] > lista1[i+1]:
        d1 = 1
    elif lista1[i] == lista1[i+1]:
        s1 = 1

c2 = 0
d2 = 0
s2 = 0

for i in range (0,(len(lista2)-1),1):
    if lista2[i] < lista2[i+1]:
        c2 = 1
    elif lista2[i] > lista2[i+1]:
        d2 = 1
    elif lista2[i] == lista2[i+1]:
        s2 = 1

c3 = 0
d3 = 0
s3 = 0

for i in range (0,(len(lista3)-1),1):
    if lista3[i] < lista3[i+1]:
        c3 = 1
    elif lista3[i] > lista3[i+1]:
        d3 = 1
    if lista3[i] == lista3[i+1]:
        s3 = 1
    
if c1 > 1:
    print('S')
if d1 > 1:
    print('S')
if s1 > 1:
    print('S')
if c2 > 1:
    print('S')
if d2 > 1:
    print('S')
if s2 > 1:
    print('S')
if c3 > 1:
    print('S')
if d3 > 1:
    print('S')
if s3 > 1:
    print('S')