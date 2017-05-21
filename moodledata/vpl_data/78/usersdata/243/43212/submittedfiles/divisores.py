# -*- coding: utf-8 -*-
import math
n=int(input('digite o n de multiplos:'))
a=int(input('digite a:))
b=int(input('digite b:))
cont=0
i=1
i=i+1
while cont<n:

    if i%a==0 or i%b==0:
        cont=cont+1
        print(i)
    