# -*- coding: utf-8 -*-
from __future__ import division

a = int(input("Digite o número: "))

cont = 0
z = 1
x = a%2

while a>0:
    d = a%2
    a = a/2
    cont = cont + x*z
    z = z*10
print ("%x"%cont)
