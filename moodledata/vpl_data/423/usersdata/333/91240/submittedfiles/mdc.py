# -*- coding: utf-8 -*-
import math
a = int(input("Digite a:? "))
b = int(input("digite b:? "))
x=1
while (x <=a ):
    if(a%x)==0 and (b%x)==0:
         MDC=x
    x = x + 1
print(MDC)
