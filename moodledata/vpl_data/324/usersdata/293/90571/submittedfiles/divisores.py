# -*- coding: utf-8 -*-
import math
a=int(input("Digite a: "))
b=int(input("Digite b: "))
n=int(input("Digite n: "))
if a>b:
    print(b)
    print(a)
    for i in range(0,(n-2)/2,1):
        b=b+b
        print(b)
        a=a+a
        print(a)