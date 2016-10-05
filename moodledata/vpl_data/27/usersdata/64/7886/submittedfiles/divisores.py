# -*- coding: utf-8 -*-
from __future__ import division
import math

n = int(input("Digite o valor de n: "))
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))

i = 1
j = 0

while i<n:
    if j % a == 0 or j % b == 0 :
        print (i)
    
        i = i + 1
    
    
        