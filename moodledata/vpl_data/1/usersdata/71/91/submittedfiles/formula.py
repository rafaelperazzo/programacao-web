# -*- coding: utf-8 -*-
from __future__ import division

P = input("Insira um valor para P: ")
i = input("Insira um valor para i: ")
n = input("Insira um valor para n: ")

v = P*(((1+i)**n-1)/i)

print("%.2f" %v)