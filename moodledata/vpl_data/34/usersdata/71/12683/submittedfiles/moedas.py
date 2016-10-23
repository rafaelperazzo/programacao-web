# -*- coding: utf-8 -*-
from __future__ import division

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

qa=c//a
resto=c-(qa*a)
qb=resto//b

if ((qa*a)+(qb*b))==c:
    print qa
    print qb
else:
    print "N"