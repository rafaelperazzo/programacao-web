# -*- coding: utf-8 -*-
import math
l1=int(input('digite um numero: '))
l2=int(input('digite um numero: '))
l3=int(input('digite um numero: '))
l4=int(input('digite um numero: '))
while (l1<l2) or (l1>l2) or (l2<l3) or (l3<l2) or (l1<l3) or (l3<l1):
    print ('S')
    break
if l1==l2==l3==l4:
    print ('N')