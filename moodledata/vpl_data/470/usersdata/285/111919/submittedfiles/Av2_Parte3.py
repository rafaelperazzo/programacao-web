# -*- coding: utf-8 -*-
a = int(input('digite o valor de a: '))
b = int(input('digite o valor de b: '))
q = int(input('digite o valor de q: '))
c=0
i=2
while i<=q:
    if a%i==0 and b%i==0:
        c = c + i
    i = i + 1
print(c)    