# -*- coding: utf-8 -*-
from __future__ import division
import math

n= input (int ('Digite n:'))
contador = 1
i = 10

while (i<n):
    if (n//i>0):
        contador = contador+1
    
    i=i*10
        
print (contador)
