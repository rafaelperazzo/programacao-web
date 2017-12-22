# -*- coding: utf-8 -*-
import math
a=int(input("Digite a: "))
b=int(input("Digite b: "))
n=int(input("Digite n: "))
if a>b and n%2==0:
    print(b)
    print(a)
    for i in range(0,(n-2)/2,1):
        b=b+b
        print(b)
        a=a+a
        print(a)
elif b>a and n%2==0:
    print(a)
    print(b)
    for i in range (0,(n-2)/2,1):
        a=a+a
        print(a)
        b=b+b
        print(b)
elif a>b and n%2!=0:
    print(b)
    print(a)
    for i in range (0,(n-2)/2,1):
        b=b+b
        print(b)
        a=a+a
        print(a)
    print(b+b)
elif a<b and n%2!=0:
    print(a)
    print(b)
    for i in range(0,(n-2)/2,1):
        a=a+a
        print(a)
        b=b+b
        print(b)
    print(a+a)