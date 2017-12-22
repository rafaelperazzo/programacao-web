# -*- coding: utf-8 -*-

n=int(input('Digite n : '))
a=[]
x9=0

for i in range (0,n,1):
    T=int(input('Digite T : '))
    a.append(T)

for i in range (1,len(a),1):
    soma = abs(a[i-1] - a[i])
    if soma> x9:
        degrau1= a[i-1]
        degrau2= a[i]
        
print(degrau1)
print(degrau2)
    
