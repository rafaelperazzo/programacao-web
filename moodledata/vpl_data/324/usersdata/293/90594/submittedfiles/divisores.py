# -*- coding: utf-8 -*-
import math
n=int(input("Digite n: "))
a=int(input("Digite a: "))
b=int(input("Digite b: "))
multipleA=0
multipleB=0
if a<b and n%2==0:
    for i in range (0,n/2,1):
        multipleA= multipleA + a
        print(multipleA)
        multipleB= multipleB + b
        if multipleA==multipleB:
            break
        else:
            print(multipleB)
    
    