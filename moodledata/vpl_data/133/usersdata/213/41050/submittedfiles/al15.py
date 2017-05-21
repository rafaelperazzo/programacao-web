# -*- coding: utf-8 -*-
for i in range(1000,10000,1):
    divisao=i//100
    restoDivisao=i%100
    n=divisao+restoDivisao
    if i**(1/2) == n:
        print(i)