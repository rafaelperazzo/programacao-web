# -*- coding: utf-8 -*-
from __future__ import division
import math
m=input("digite m:")
soma=0
deno=2
termo=1
while termo<=m:
    if termo%2==0:
        soma=soma -(4/((deno)*(deno+1)*(deno+2)))
    else:
        soma=soma + (4/((deno)*(deno+1)*(deno+2)))
    deno=deno+2
    termo=termo+1
soma=soma+3
print soma
    
