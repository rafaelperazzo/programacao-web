# -*- coding: utf-8 -*-
n=int(input('Digite n: '))
m=int(input('Digite m: '))
a=[]
b=[]
for i in range(0,n,1):
    a.append(int(input('Digite elementos de a: ')))
for i in range(0,m,1):
    b.append(int(input('Digite ementos de b: ')))

cont=0    
while n<m or m<n:
    if len(a) in len(b):
        cont+=1
print(cont)    
    
