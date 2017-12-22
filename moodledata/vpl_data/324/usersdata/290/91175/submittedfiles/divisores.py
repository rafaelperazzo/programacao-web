# -*- coding: utf-8 -*-
import math
n=int(input("Digite o valor de n: "))
a=int(input("Digite o valor de a: "))
b=int(input("Digite o valor de b: "))
p=1
c=a*b
d=b
e=1
while p<=n/2:
    a=a*p
    b=b*p
    c=c*p
    if a<b and a!=e:
        if a!=c and b!=c:
            print(a)
            print(b)
            c=c/p
        if b==c:
            print(a)
            print(b)
            e=b
    p=p+1