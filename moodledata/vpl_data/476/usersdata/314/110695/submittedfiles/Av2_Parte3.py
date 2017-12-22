# -*- coding: utf-8 -*-
a=[]
b=[]

n=int(input('Digite o tamanho de a:'))
m=int(input('Digite o tamanho de b:'))

for i in range(0,n,1):
    a.append(int(input('Digite os elementos de a: ')))
for j in range(0,m,1):
    b.append(int(input('Digite os elementos de b: ')))
    
    
cont=0    

if b[i] in a[i]:
    cont+=1

print(cont)    