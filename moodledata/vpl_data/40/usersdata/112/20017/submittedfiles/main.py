# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

def fatorial(n):
    count=n
    result=1
    while count>1:
        result*=count
        count-=1
    return result