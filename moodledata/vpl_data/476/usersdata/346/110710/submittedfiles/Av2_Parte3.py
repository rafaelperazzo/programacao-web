# -*- coding: utf-8 -*-

n= int(input('Digite n: '))
m= int(input('Digite m: '))

a=[]
for i in range(0,n,1):
    a.append(input('n= '))
    
b=[]
for j in range(0,m,1):
    b.append(input('m= '))
    
    
cont= 0
for i in range(0,len(a),1):
    for j in range(0, len(b),1):
        if a[i]==b[j]:
            cont += 1

print(cont)
    

    
    

