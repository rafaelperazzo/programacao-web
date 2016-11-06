# -*- coding: utf-8 -*-
from __future__ import division

a = int(input("Digite a:"))
b = int(input("Digite a:"))
c = int(input("Digite a:"))

ca = c//a
cb = c//b
cca = c%a
ccb = c%b

if c%a!=0 and c%b!=0:
    qa = ca
    print(qa)
    qb = cca//b
    print(qb)
    
    if c%b!=0 and c%a!=0 or c%a==0:
        qa = ccb//a
        print(qa)
        qb = cb
        print(qb)