# -*- coding: utf-8 -*-
n=int(input('digite numero de pessoa:'))
x=int(input('instante em que a pessoa passou:'))
a=x
cont=10
for i in range(2,n+1,1):
    t=int(input('instante em que a pessoa passou:'))
    b=(t-a)
    cont=cont+b
    a=t
print(contador)