# -*- coding: utf-8 -*-
a=int(input('número de pessoas:'))
b=int(input('instante em que a pessoa passou:'))
x=b
cont=10
for i in range(2,a+1,1):
    t=int(input('instante em que passou:'))
    b=(t-a)
    cont=cont+b
    a=t
print(cont)