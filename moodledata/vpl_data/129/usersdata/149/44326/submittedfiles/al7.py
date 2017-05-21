# -*- coding: utf-8 -*-
n=int(input('digite o valor de n:'))
i=0
soma=0
for i in range(1,n,1):
    if n%i==0:
        j=n//i+i
        print(i)
        soma=soma+j
if j==n:
    print(PERFEITO)
