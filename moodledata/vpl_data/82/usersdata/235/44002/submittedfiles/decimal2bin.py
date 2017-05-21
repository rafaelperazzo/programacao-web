# -*- coding: utf-8 -*-
n=int(input('digite seu numero:'))
s=0
i=0
while (n/10)>0:
    a=n%10
    s=s+(a*(2**i))
    n=n//10
    i=i+1
print(s)

