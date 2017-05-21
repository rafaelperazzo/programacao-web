# -*- coding: utf-8 -*-
import math
a=int(input("Digite a: "))
b=int(input("Digite b: "))
n=int(input("Digite n: "))
x=0
while x!=n:
    if x%a == 0 or x%b == 0:
        print(x)
    x=x+1    

