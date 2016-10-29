# -*- coding: utf-8 -*-
from __future__ import division
a=input("Digite o valor da primeira moeda:")
b=input("Digite o valor da segunda moeda:")
c=input("Digite o valor em cedulas:")

d=c//a
e=c//b

if c%a==0:
    print(d)
    print("0")
elif c%b==0:
    print("0")
    print(e)

