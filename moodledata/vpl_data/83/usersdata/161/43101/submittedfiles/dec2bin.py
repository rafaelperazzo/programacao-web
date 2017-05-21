# -*- coding: utf-8 -*-
n=int(input('Digite um número decimal:'))
i=0
s=0
while n>0:
    resto=n%2
    s=s+resto*10**i
    n=n//2
print(s)    

