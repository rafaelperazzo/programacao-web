# -*- coding: utf-8 -*-
import math
n=int(input("Digite n: "))
a=int(input("Digite a: "))
b=int(input("Digite b: "))
x=1
h=0
while h!=n :
    if x%a == 0 or x%b == 0:
        print(x)
        h=h+1
    x=x+1
    

    

