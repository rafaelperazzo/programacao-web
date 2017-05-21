# -*- coding: utf-8 -*-
import math
a=int(input("Digite o primeiro numero: "))
b=int(input("Digite o segundo numero: "))
mdc=a
while a%mdc != 0 or b%mdc !=0:
    mdc=mdc+1
print(mdc)
