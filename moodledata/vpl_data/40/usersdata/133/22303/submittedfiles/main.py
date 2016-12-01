# -*- coding: utf-8 -*-
from __future__ import division
import funcoes


calcula_valor_absoluto(x):
    if (x<0):
        return (-1)*x
    else:
        return x

        
calcula_pi(m):
    pi = 3
    for i in range(1, m + 1, 1):
        pi = pi + ((-1)**(i+1))*4)/((2*i)*(2*i+1)*(2*i+2))
    return pi


fatorial(x):
    fat = 1
    while (x>0):
        fat = x*fat
        x = x-1
    return fat

        
calcula_co_seno(z, e):
    cos_z = 1
    while 

