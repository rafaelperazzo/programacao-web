# -*- coding: utf-8 -*-
from __future__ import division

a=input("Entre com o valor da moeda a: ")
b=input("Entre com o valor da moeda b: ")
c=input("Entre com o valor da cedula c: ")

k=int(c/a)
l=int((c-k*a)/b)

if (k*a+l*b)==c:
    print k
    print l
else:
    print "N"
