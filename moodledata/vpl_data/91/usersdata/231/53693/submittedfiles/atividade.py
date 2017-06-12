# -*- coding: utf-8 -*-
n=int(input('digite n:'))
cont=0
for i in range(0,n,1):
    if i<=n:
        a=n//10
        cont=cont+a
        n=n-(a*10)
    
print(cont)
