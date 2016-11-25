# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

#COMECE AQUI

def calculo_pi(m):
    i = 1
    soma = 0
    j = 1
    while i<=m:
        if i%2==0:
            soma = soma - 4/j
        else:
            soma = soma + 4/j
        
        j = j + 2
        i = i + j
return True

print calculo_pi(m)



