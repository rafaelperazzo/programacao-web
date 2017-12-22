# -*- coding: utf-8 -*-
import math
x = int(input('Digite o primeiro numero: '))
y = int(input('Digite o segundo numero: '))
i = x + y
while True:
    i -= 1
    if (x%i)==0 and (y%i)==0:
        break
print (i)
