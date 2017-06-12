# -*- coding: utf-8 -*-
n=int(input('digite n:'))
m=int(input('digite m:'))
x=m
cont=10
for i in range(2,n+1,1):
    t=int(input('digite tempo:'))
    a=t-x
    cont=cont+a
    x=t
print(cont)