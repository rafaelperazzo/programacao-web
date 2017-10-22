# -*- coding: utf-8 -*-
soma=0
i=0
while (n>0):
    ultimo=n%10
    s=s+(ultimo*(2**i))
    i=i+1
    n=n//10
print (s)

