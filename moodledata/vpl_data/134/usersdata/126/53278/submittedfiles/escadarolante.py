# -*- coding: utf-8 -*-
n=int(input('digite o numero de pessoas que passaram pelo sensor:'))
a=[]
i=0
m=0
soma=0
if n>0:
    for i in range(1,n+1,1):
        m=int(input('digite o instante em que a pessoa passou pelo sensor:'))
        a.append(m)
        i=i+1
for i in range(0,len(a)-1,1):
    soma=soma+a[i+1]-a[i]
    i=i+1
soma=soma+10
print(soma)