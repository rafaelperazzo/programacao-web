# -*- coding: utf-8 -*-

a=int(input('Digite a : '))
b=int(input('Digite b : '))
i=a
while(i>0):
    if a%i==0 and b%i==0:
        print(i)
        break
    else:
        i=i-1