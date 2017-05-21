# -*- coding: utf-8 -*-
import math
n1=int(input('coloque o valor do primeiro numero:'))
n2=int(input('coloque o valor do segundo numero:'))
if n2<=n1:
    n=n2
else:
    n=n1
cont=0
while cont!=1:
    if (n1%n)==0 and (n2%n)==(n1%n):
        cont=1
        mdc=n
    else:
        n=n-1
print(n)