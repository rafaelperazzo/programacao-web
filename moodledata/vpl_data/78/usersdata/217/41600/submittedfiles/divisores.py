# -*- coding: utf-8 -*-
import math
n=int(input("Digite n: "))
a=int(input("Digite a: "))
b=int(input("Digite b: "))
cont=0 
m=1
while cont < n:
    if m%a==0 or m%b==0:
        print(m)
        cont += 1
    m += 1