# -*- coding: utf-8 -*-
from __future__ import division

a = input("Insira um Número: ")
b = input("Insira Outro Número: ")
i = 1

while i<=a*b:
    if i%a==0 and i%b==0:
        mmc=i
    i=i+1
    
print mmc
