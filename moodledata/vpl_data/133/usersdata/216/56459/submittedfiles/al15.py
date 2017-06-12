# -*- coding: utf-8 -*-

for i in range(1000,9999+1,1):
    x=i//100
    y=i%100
    soma=x+y
    if ((i)**(1/2))==(soma):
        print(i)
