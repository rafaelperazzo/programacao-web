# -*- coding: utf-8 -*-

a= []
n= int(input('Digite um valor para n: '))
for i in range(0,n,1):
    a.append(int(input('Digite um valor: ')))
   

b= []
m= int(input('Digite um valor para m: '))
for i in range(0,m,1):
    b.append(int(input('Digite um valor: ')))
   
print set(a).intersection(b)
len(set)

