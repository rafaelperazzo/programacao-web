# -*- coding: utf-8 -*-
import math
n1=int(input('Digite o valor do número 1: '))
n2=int(input('Digite o valor do número 2: '))
mdc=1
if n1%n2==0:
    resto=2
while n1%n2!=0:
    resto=n1%n2
    mdc=mdc+1
    n1=n2
    n2=resto

print(resto)
print(mdc)

