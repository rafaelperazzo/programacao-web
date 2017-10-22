# -*- coding: utf-8 -*-
import math
x = int(input("Digite o primeiro número: "))
while x < 0 and x!=0:
    x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))
while y < 0 and y!=0:
    y = int(input("Digite o segundo número: "))
mdc = x
while x % mdc!=0:
    mdc = mdc - 1
    print (mdc)
    
