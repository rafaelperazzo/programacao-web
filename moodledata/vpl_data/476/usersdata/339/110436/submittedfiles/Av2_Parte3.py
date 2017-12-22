# -*- coding: utf-8 -*-
a=[]
b=[]
n=int(input('quantidade de elementos a: '))
m=int(input('quantidade de elementos b: '))

for i in range(n):
    a.append(input('Elementos de a: '))
    
for i in range(m):
    b.append(input('Elementos de b: '))
    
e=0
while a in b:
    e+=1

print (e)