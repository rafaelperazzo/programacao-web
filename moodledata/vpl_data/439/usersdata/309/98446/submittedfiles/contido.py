# -*- coding: utf-8 -*-

n=int(input("Digite a quantidade de elementos de A:"))
m=int(input("Digite a quantidade de elementos de B:"))

a=[]
b=[]

for i in range (0, n, 1):
    a.append(int(input("Digite o %dº elemento de A:" %(i+1))))

for i in range (0, m, 1):
    a.append(int(input("Digite o %dº elemento de B:" %(i+1))))   

c=[]
if (n>m):
    for z in range (0, n, 1):
        for i in range (0, m, 1):
            if (a[z]==b[i]):
             c.append(a[z])
            
else: 
    for i in range (0, m, 1):
        for z in range (0, n, 1):
            if (a[z]==b[i]):
             c.append(a[z])
            
            
qua=len(c)            