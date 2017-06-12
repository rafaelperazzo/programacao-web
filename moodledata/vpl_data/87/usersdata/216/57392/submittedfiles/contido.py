# -*- coding: utf-8 -*-


m=int(input('Digite a quantidade de a:'))
l=int(input('Digite a quantidade de b:'))
a=[]
b=[]

for i in range(0,m,1):
    n=int(input('Digite o valor:'))
    a.append(n)
    
for i in range(0,l,1):
    j=int(input('Digite o valor:'))
    b.append(j)
    
for i in range(0,m,1):
    if b[i]==a[i]:
        cont=con+1
        
print(cont)
print(a)
print(b)
