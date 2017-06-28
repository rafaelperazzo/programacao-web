# -*- coding: utf-8 -*-
n = int(input('Digite a quantidade de degrais:' ))
a = []
for i in range(1,n+1,1):
    a.append(int(input('Digite o valor do %dº degrau: '%i)))

for i in range(0,n-1,1):
    b=[]
    soma=a[i]-a[i+1]
    if soma<0:
        soma=soma*(-1)
    b.append(soma)

print len(b)