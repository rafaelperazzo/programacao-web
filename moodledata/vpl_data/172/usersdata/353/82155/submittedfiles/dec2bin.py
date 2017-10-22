# -*- coding: utf-8 -*-
n=int(input('Valor de n:'))
e=0
s=0
while (n>0):
    resto=n%2
    s=s+(resto*(10**e))
    n=n//2
    e=e+1
print (s)

