# -*- coding: utf-8 -*-
n=int(input('Binário: '))
i=0
s=0
while n>0:
    s=s+(2**i)*(n%10)
    n=n//10
    i=i+1
print(s)

