# -*- coding: utf-8 -*-
from __future__ import division

a = int(input("Digite valor de a: "))
b = int(input("Digite valor de b: "))
c = int(input("Digite valor de c: "))

d=c/a
e=c/b
f=c%a
g=c%b

if c%a==0:
    qa=d
    print(qa)
    print("0")

elif c%a!=0:
    print("0")
    qb=e
    print(qb)