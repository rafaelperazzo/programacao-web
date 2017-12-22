# -*- coding: utf-8 -*-
import math
n=int(input("Digite o valor de n: "))
a=int(input("Digite o valor de a: "))
b=int(input("Digite o valor de b: "))
p=1
c=a*b
d=b
while p<=n/2:
    a=a*p
    b=b*p
    c=c*p
    if a<b:
        if a!=c or b!=c:
            print(a)
            print(b)
            c=c/p
        if a==c:
            print(a)
            if a*(p+1)<b:
                print(a*(p+1))
            else:
                print(b)
        if b==c:
            print(b)
            print(a*(p+1))
    p=p+1