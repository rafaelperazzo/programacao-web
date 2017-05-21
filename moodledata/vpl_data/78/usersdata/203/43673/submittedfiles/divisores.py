# -*- coding: utf-8 -*-
import math
n=int(input('digite n: '))
a=int(input('digite a: '))
b=int(input('digite b: '))
cont=0
i=1
while cont<n:
    Ma=a*i
    Mb=b*i
    if Ma<Mb:
        print(Ma)
        i=i+1
    else:
        print(Mb)
        i=i+1
    cont=cont+1