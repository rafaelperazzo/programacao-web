# -*- coding: utf-8 -*-
import math
n=int(input('digite n: '))
a=int(input('digite a: '))
b=int(input('digite b: '))
cont=0
i=2
Ma=a
Mb=b
while cont<n:
    if Ma<Mb:
        print(Ma)
        Ma=a*i
        print(Mb)
    if Mb<Ma:
        print(Mb)
        Mb=b*i
        print(Ma)
    else:
        print(Ma)
    cont=cont+1