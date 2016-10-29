# -*- coding: utf-8 -*-
from __future__ import division
n=input('Digite o número que deseja transformar:')
i=0
result=n*4//2
while n//2!=1:
    n=result
    result=n//2
    resto=result%2
    print(result)