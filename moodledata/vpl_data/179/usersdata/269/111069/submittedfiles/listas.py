# -*- coding: utf-8 -*-
n=int(input('digite n: '))
a=[]
for p in range(0,n,1):
    x=int(input('digite valor: '))
    a.append(x)
for i in range(0,len(a)-2,1):
    if (((a[i]-a[i+1])**2)**0.5) > (((a[i+1]-a[i+2])**2)**0.5:
        save = (((a[i]-a[i+1])**2)**0.5)
    else:
        save = (((a[i+1]-a[i+2])**2)**0.5)
print(save)        
    
