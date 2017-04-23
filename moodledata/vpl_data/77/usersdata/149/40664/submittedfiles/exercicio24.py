# -*- coding: utf-8 -*-
import math
a=int(input('Digite a:'))
b=int(input('Digite b:'))


for c in range(1,a+1,1):
    if a%c==0:
        print(c)
for d in range(1,b+1,1):
    if b%d==0:
        print(d)

if c==d:
    print(c)

