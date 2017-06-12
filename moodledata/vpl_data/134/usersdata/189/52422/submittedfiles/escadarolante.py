# -*- coding: utf-8 -*-
a=int(input('número de pessoas:'))
b=int(input('instante em que a pessoa passou:'))
x=b
cont=10
for i in range(2,a+1,1):
    t=int(input('instante em que passou:'))
    y=(t-x)
    cont=cont+y
    x=t
print(cont)