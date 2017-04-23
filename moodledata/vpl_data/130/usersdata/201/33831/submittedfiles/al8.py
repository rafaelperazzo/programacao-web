# -*- coding: utf-8 -*-
n=int(input('Digite um número:'))
fatorial=1
i=1
for i in range(1,n+1,1):
    fatorial=fatorial*i
    i=i+1
print(fatorial)
