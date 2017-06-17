# -*- coding: utf-8 -*-

def degrau(a):
    for i in range(0,len(a)-1,1):
        a.append(a[i]-a[i-1])
        
a=[]
n=int(input('digite n:'))
for i in range(0,n,1):
    valor=int(input('digite valor:'))
    a.append(valor)
print(a)




