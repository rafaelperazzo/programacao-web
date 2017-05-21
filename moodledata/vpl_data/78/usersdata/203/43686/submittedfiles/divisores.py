# -*- coding: utf-8 -*-
import math
n=int(input('digite n: '))
a=int(input('digite a: '))
b=int(input('digite b: '))
cont=0
i=1
Ma=a
Mb=b
while cont<n:
    if Ma<Mb:
        print(Ma)
        Ma=Ma+a*i
        i=i+1
    else:
        print(Mb)
        Mb=Mb+b*i
        i=i+1
    cont=cont+1