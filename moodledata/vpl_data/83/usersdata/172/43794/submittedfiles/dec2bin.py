# -*- coding: utf-8 -*-
n=int(input('n'))
s=0
i=0
while n>0:
    resto=n%2
    s=s+((resto)*(10**i))
    n=n//2
    i=i+1
print(s)
