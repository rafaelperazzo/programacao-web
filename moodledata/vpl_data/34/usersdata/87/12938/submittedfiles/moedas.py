# -*- coding: utf-8 -*-
from __future__ import division

a = int(input("Digite valor de a: "))
b = int(input("Digite valor de b: "))
c = int(input("Digite valor de c: "))

if c%a==0:
    qa=c/a
    print(qa)
    print("0")

if c%a!=0:
    print("0")
    qb=c/b
    print(qb)