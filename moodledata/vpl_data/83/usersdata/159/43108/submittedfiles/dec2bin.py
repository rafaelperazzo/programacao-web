# -*- coding: utf-8 -*-
n=float(input('Digite n:'))
i=n
s=0
exp=0
while i>0:
    x=i%2
    s=s+x*(10**exp)
    i=i//2
print(s)    

