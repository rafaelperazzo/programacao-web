# -*- coding: utf-8 -*-
import math
n=int(input("Digite o valor de n: "))
a=int(input("Digite o valor de a: "))
b=int(input("Digite o valor de b: "))
p=1
c=a*b
d=b
e=1
j=0
while p<=n/2:
    a=a*p
    b=b*p
    c=c*(p-j)
    if a<b and a!=e:
        if a!=c and b!=c:
            print(a)
            print(b)
            j=j+1
        if b==c:
            print(a)
            print(b)
            e=b
    
    p=p+1
            