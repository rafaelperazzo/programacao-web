# -*- coding: utf-8 -*-
from __future__ import division
import funcoes
n=input('Digite o valor de n:')
def fatorial(n):
    count=n
    result=1
    while count>1:
        result*=count
        count-=1
    return result
print fatorial(n)