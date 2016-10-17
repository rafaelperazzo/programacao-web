# -*- coding: utf-8 -*-
from __future__ import division

a = input("Insira um Número: ")
b = input("Insira Outro Número: ")
i =2
mdc=1

while i<=a:
    if a%i==0 and b%i==0:
        mdc=i
    i=i+1
    
print mdc
    