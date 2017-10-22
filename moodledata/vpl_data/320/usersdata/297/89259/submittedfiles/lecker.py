# -*- coding: utf-8 -*-
import math
a=int(input('digite um numero inteiro: '))
b=int(input('digite um numero inteiro: '))
c=int(input('digite um numero inteiro: '))
d=int(input('digite um numero inteiro: '))
while a<1 and b<1 and c<1 and d<1 :
    a=int(input('digite um numero inteiro: '))
    b=int(input('digite um numero inteiro: '))
    c=int(input('digite um numero inteiro: '))
    d=int(input('digite um numero inteiro: '))
if a>b>=c>=d or a<b>c>=d or a<=b<c>d or a<=b<=c<d :
    print('S')
else :
    print('N')