# -*- coding: utf-8 -*-
import math
n=int(input("Digite n: "))
a=int(input("Digite a: "))
b=int(input("Digite b: "))
multipleA=0
multipleB=0
if a<b and n%2==0:
    for i in range(0,n,2):
        if multipleA!=multipleB:
            multipleA=multipleA+a
            multipleB=multipleB+b
            print(multipleA)
            print(multipleB)
elif a>b and n%2==0:
    for i  in range(0,n,2):
        multipleA=multipleA+a
        multipleB=multipleB+b
        print(multipleB)
        print(multipleA)
elif a<b and n%2!=0:
    for i in range(0,n+2,2):
        multipleA=multipleA+a
        multipleB=multipleB+b
        print(multipleA)
        print(multipleB)
elif a>b and n%2!=0:
    for i in range(0,n+2,2):
        multipleA=multipleA+a
        multipleB=multipleB+b
        print(multipleB)
        print(multipleA)