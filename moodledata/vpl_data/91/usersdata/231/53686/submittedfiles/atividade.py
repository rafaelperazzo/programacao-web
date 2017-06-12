# -*- coding: utf-8 -*-
n=int(input('digite n:'))
cont=0
for i in range(0,n,1):
    if i<=n:
        n=n//10
        cont=cont+n
    
print(cont)
