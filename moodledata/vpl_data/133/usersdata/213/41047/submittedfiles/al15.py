# -*- coding: utf-8 -*-
for i in range(1000,10000,1):
    divisao=i//10
    restoDivisao=i%10
    n=divisao+restoDivisao
    if i**(1/2) == n:
        print(i)