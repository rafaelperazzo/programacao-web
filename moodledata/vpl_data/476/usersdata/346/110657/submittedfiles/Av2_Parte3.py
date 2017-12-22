# -*- coding: utf-8 -*-

n= int(input('Digite n: '))
m= int(input('Digite m: '))

a=[]
for i in range(0,n,1):
    a.append(input('n= '))
    
b=[]
for i in range(0,m,1):
    b.append(input('m= '))

if n>m:
    c= n
else:
    c=m


for i in range(0,c+1,1):
    cont = 0
    if a[i]==b[i]:
        cont += 1

print(cont)
    

    
    

