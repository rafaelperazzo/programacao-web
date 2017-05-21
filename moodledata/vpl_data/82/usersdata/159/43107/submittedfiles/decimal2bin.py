# -*- coding: utf-8 -*-
n=int(input('Digite n:'))
i=0
s=0
while n>0:
    x=n%10
    s=s+(x*(2**i))
    i=i+1
    n=n//10
print(s)    

