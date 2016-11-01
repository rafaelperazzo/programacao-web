# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('Digite um valor:'))
p=a
cont=0
while p>0:
    p=p//10
    cont = cont +1
s = 0
for i in range(0, cont, 1):
    b=a%10
    s = s + b*(2)**i
    a = a//10
print(s)

