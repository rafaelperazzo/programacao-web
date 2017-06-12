# -*- coding: utf-8 -*-
n=int(input('digite n:'))
a=[]
for i in range(1,n+1,1):
    inst=int(input('digite inst:'))
    a.append(inst)
soma=0
for i in range(len(a)-1,0,-1):
    b=a[i]-a[i-1]
    soma=soma+b
t=soma+10
print(t)