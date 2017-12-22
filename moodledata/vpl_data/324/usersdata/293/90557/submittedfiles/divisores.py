# -*- coding: utf-8 -*-
import math
a=int(input("Digite a: "))
b=int(input("Digite b: "))
n=int(input("Digite n: "))
if a>b:
    for i in range(1,n,1):
        print(b)
        print(a)
        a=a+a
        b=b+b
    print(b)
    print(a)

