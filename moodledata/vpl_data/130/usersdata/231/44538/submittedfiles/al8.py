# -*- coding: utf-8 -*-
n=int(input('digite valor de n :'))
cont=0
for i in range(1,n+1,1):
    v=i*(n-(i+1))
    cont=cont+v

print(cont)




