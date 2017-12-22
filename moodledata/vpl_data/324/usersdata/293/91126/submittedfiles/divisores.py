# -*- coding: utf-8 -*-
import math

a=int(input("Digite a: "))
b=int(input("Digite b: "))
n=int(input("Digite n: "))

multipleA=0
multipleB=0
for i in range(1,n,1):
    multipleA=multipleA+a
    multipleB=multipleB+b
    if multipleA!=multipleB:
        print multipleA
    else:
        print multipleB