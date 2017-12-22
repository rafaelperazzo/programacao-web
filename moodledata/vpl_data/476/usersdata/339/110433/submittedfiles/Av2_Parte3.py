# -*- coding: utf-8 -*-
a=[]
b=[]
n=int(input('quantidade de elementos a: '))
m=int(input('quantidade de elementos b: '))

for i range(0,n):
    a.append(input('Elementos de a: '))
    
for i range(0,m):
    b.append(input('Elementos de b: '))
    
e=0
while a in b:
    e+=1

print (e)