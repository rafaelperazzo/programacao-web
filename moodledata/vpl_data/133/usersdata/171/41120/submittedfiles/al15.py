# -*- coding: utf-8 -*-
for i in range(1000,10000,1):
    x=i/100
    a=('%d'%x)
    b=('%f'%x)
    if i**0.5==a+b:
        print(i)