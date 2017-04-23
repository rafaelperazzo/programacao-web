# -*- coding: utf-8 -*-
n=int(input('Digite o valor de n:'))
i=2
while i<n:
    if n%i==0:
        print(i)
    i=i+1
    if n%i!=0: