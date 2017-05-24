# -*- coding: utf-8 -*-
import math
a=int(input("Digite a: "))
b=int(input("Digite b: "))
c=int(input("Digite c: "))
n=1
p=0
o=0
while p==0:
    if (n%a)==0 and (n%b)==0 and (n%c)==0:
        o=o+n
        p=p+1
    else:
        n=n+1
print(o)