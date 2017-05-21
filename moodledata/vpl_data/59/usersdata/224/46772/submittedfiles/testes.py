# -*- coding: utf-8 -*-
import math
n=int(input('Digite n: '))
soma=0
i=0
    soma=soma+(n//10)*2**i
    n=n%10
    i=i+1
print(soma)