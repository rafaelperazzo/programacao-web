# -*- coding: utf-8 -*-
import math
n=int(input('Digite n: '))
soma=0
i=0
while n//10>0:
    resto=n%2
    soma=soma+resto*10**i
    n=n//2
    i=i+i
print(soma)