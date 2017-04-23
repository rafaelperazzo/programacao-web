# -*- coding: utf-8 -*-
import math
n1=int(input('digite o primeiro valor: '))
n2=int(input('digite o segundo valor: '))
i=2
while i<=n1:
    if n1%i==0 and n2%i==0:
        cont=i
        if i>cont:
            print(cont)
        