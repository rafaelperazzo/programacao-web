# -*- coding: utf-8 -*-
n=int(input('Quantidade de pessoas detectadas pelo sensor:'))
a=[]
for i in range(1,n+1,1):
    instante=int(input('%dºInstante:'%i))
    a.append(instante)
for i in range(len(a)-1,0,-1):
    b=a[i]-a[i-1]
t=b+10
print(t)