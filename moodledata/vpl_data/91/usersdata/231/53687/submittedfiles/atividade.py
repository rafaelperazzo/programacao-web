# -*- coding: utf-8 -*-
n=int(input('digite n:'))
cont=0
for i in range(0,n,1):
    if i<=n:
        v=n//10
        cont=cont+v
        n=n-(v*10)
    
print(cont)
