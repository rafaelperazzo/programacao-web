# -*- coding: utf-8 -*-
import math
a = int(input('Digite valor de a: '))
while a <0:
    a = int(input('Digite valor de a: '))
    
b = int(input('Digite valor de b: '))
while b <0:
    b = int(input('Digite valor de b: '))


if a>b:
    c = a
else:
    c = b

while True:
    if a%c == 0 and b%c == 0:
        print (c)
        break
    else:
        c = c-1