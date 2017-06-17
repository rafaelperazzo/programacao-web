# -*- coding: utf-8 -*-

def degrau(a):
    cont=0
    for i in range(0,len(a)-1,1):
        if (a[i]-a[i-1])>a([i+1]-a[i+2]):
            cont=cont+(a[i]-a[i-1])
        else:
            cont=cont+a([i+1]-a[i+2])
    return cont
    
        
a=[]
b=[]
n=int(input('digite n:'))
for i in range(0,n,1):
    valor=int(input('digite valor:'))
    a.append(valor)
print(degrau(a))




