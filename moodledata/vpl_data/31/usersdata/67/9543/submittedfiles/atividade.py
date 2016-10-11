# -*- coding: utf-8 -*-
from __future__ import division
import math

n=int(input("Digite o valor de n:"))
i=1
while (i<=n):
    x=input("Digite o valor de x:")
    y=input("Digite o valor de y:")
    if x>=0 and y>=0 and (x**2)+(y**2)<=1:
        print("'SIM'")
    else:
        print("'NÃO'")
        
    i=i+1