# -*- coding: utf-8 -*-
import math
a=int(input('Digite um inteiro a: '))
b=int(input('Digite um interro b: '))
n=int(input('Digite a qunatidade de multiplos n: '))
i=1
while i<n:
    c=a*i
    d=b*i
    i+=1
    if c!=d:
        print (c)
    if d!=c:
        print (d)
   