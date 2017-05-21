# -*- coding: utf-8 -*-
n=int(input('Digite um número na base binária:'))
i=0
s=0
while n>0:
    resto=n%10
    s=s+resto*2**i
    n=n//10
    i=i+1
print(s)    

