# -*- coding: utf-8 -*-
import math
n=int(input("Digite o valor de n: "))
a=int(input("Digite o valor de a: "))
b=int(input("Digite o valor de b: "))
p=1
c=a
d=b
if a<b:
    for i in range(1,(n/2)+1,1):
        if a*i!=a*b:
            c=c*i
            d=d*i
            print(c)
            print(d)
    