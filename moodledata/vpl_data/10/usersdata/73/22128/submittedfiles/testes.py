# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np 
def par(x):
    return (x%2==0)
def parimpar (x):
    if par(x):
        return 'par'
    else:
        return 'impar'
print ( parimpar(4))
print ( parimpar(5))
        