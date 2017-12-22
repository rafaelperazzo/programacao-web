# -*- coding: utf-8 -*-
import math
n=int(input("Digite o valor de n: "))
a=int(input("Digite o valor de a: "))
b=int(input("Digite o valor de b: "))
c=1
i=1
while c<=n:
    if i%a==0 or i%b==0:
        print(i)
        c=c+1
    i=i+1