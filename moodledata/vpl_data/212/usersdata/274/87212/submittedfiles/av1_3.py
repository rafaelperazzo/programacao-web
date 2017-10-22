# -*- coding: utf-8 -*-
import math
a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))
c = int(input("Terceiro número: "))
i = 1
n = 1
e = 1
while (a!=b) and (b!=c):
    a=a*i  b=b*n  c=c*e
    i=i+1
    n=n+1
    e=e+1
print(a)
    

