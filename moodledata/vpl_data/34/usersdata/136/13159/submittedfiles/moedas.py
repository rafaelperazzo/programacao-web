# -*- coding: utf-8 -*-
from __future__ import division
a = int(input("Digite o valor de a:"))
b = int(input("Digite o valor de b:"))
c = int(input("Digite o valor de c:"))

ca = c//a
cb = c//b
cca = c%a
ccb = c%b

if c%a!=0 and c%b==0 or c%b!=0:
    qa = ca
    print(qa)
    qb = cca//b
    print(qb)
    
    if c%b!=0 and c%a!=0 or c%a==0:
        qa = ccb//a
        print(qa)
        qb = cb
        print(qb)
if c%a!=0 and c%b!=0:
    print("N")