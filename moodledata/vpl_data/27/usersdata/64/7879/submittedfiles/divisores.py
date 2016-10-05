# -*- coding: utf-8 -*-
from __future__ import division
import math

n = int(input("Digite o valor de n: "))
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))

i = 1

while a % i != 1 or b % i != 1 :
    
    i = i + 1
    
    n = n - 1
    
    if n <= n and n >= 0:
    
        print (i)