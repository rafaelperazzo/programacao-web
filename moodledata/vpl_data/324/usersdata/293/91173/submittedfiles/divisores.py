# -*- coding: utf-8 -*-
import math

a=int(input("Digite a: "))
b=int(input("Digite b: "))
n=int(input("Digite n: "))

multipleA=0
multipleB=0
if a<=b: 
    for i in range(0,n//2,1):
        multipleA=multipleA+a
        multipleB=multipleB+b
        if (multipleA+a)!=multipleB:
            print multipleA
            print multipleB
        else:
            print(multipleA)
            multipleA=multipleA+a
            print(multipleB)
elif a>=b:
    for i in range(0,n//2,1):
        multipleA=multipleA+a
        multipleB=multipleB+b
        if (multipleB+b)!=multipleB:
            print multipleB
            print multipleA
        else:
            print(multipleB)
            multipleA=multipleA+a
            print(multipleB)