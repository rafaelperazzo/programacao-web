# -*- coding: utf-8 -*-
n=int(input('digite o numero de pessoas que passaram pelo sensor:'))
p=int(input('digite o intante em que a pessoa passou pelo sensor:'))
m=0
t=0
i=0
for i in range(1,n,1):
    m=int(input('digite o instante em que a pessoa passou pelo sensor:'))
    t=(m-p)+10
    i=i+1
print(t)