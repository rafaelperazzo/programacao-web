# -*- coding: utf-8 -*-
import math
x=int(input('Digite um numero x: '))
y=int(input('Digite um numero y: '))
resto=(x%y)
while (resto)!=0:
    a=(y//resto)
    if y<a:
        break
print ('%d' %a)
