# -*- coding: utf-8 -*-
import math

n1=int(input('n1: '))
n2=int(input('n2: '))


while n1%.2==0 or n2%.2==0 :
    n1 = n1/2
    n2 = n2/2
    print(n1 , n2)
    if n1%.2!=0:
        break






