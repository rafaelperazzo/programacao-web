# -*- coding: utf-8 -*-
import math
a=int(input("Digite a: "))
b=int(input("Digite b: "))
c=int(input("Digite c: "))
n=1
c=n
o=0
while n==c:
    if (n%a)==0 and (n%b)==0 and (n%c)==0:
        o=o+n
        c=c+1
    else:
        n=n+1
print(o)