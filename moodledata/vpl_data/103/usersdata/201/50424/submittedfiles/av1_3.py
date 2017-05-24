# -*- coding: utf-8 -*-
import math
x=int(input('Digite um número'))
y=int(input('Digite um número'))
post=x
at=y
cont=0
res=post%at
while res!=0:
    post=at
    at=res
    res=post%at
    print(at)
    print(res)