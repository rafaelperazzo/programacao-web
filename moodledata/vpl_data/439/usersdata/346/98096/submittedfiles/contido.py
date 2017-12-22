# -*- coding: utf-8 -*-

a= []
n= int(input('Digite um valor: '))
for i in range(0,n,1):
    a.append(int(input('Digite um valor: ')))
   

b= []
m= int(input('Digite um valor: '))
for i in range(0,m,1):
    b.append(int(input('Digite um valor: ')))
   
def intersection():
    print set(a).intersection(b)
    print(len(set))

