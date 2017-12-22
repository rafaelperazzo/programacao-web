# -*- coding: utf-8 -*-
import math
n=int(input("Digite n: "))
a=int(input("Digite a: "))
b=int(input("Digite b: "))
multipleA=0
multipleB=0

for i in range(0,n,2):
    multipleB=multipleB+b
    if multipleA==multipleB:
        multipleA=multipleA+a
        print(multipleA)    
        continue
    else:
        print(multipleB)
        
        