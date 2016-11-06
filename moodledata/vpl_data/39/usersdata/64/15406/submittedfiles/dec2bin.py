# -*- coding: utf-8 -*-
from __future__ import division

a = int(input("Digite o número: "))

cont = 0
z = 1
x = n%2

while n>0:
    d = n%2
    n = n//2
    cont = cont + x*z
    z = z*10
print ("%x" %cont)
