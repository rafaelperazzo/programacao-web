# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

def fatorial(n):
    for i in range(0,n+1,1):
        n=n*n
    return n

print fatorial(3)