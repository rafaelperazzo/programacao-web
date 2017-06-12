# -*- coding: utf-8 -*-
n=input(input('digite n:'))
cont=0
for i in range(0,n,1):
    if i<=n:
        n=n//10
        cont=cont+n
    i=i+1
print(cont)
