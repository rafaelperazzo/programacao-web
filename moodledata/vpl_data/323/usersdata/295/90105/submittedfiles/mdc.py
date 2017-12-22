# -*- coding: utf-8 -*-
import math
x = int(input("Digite o primeiro numero :"))
while x < 0 and x!=0:
    x = int(input("Digite o primeiro numero :"))
y = int(input("Digite o segundo numero :"))
while y < 0 and y!=0:
    y = int(input("Digite o segundo numero :"))
mdc = x
while x%mdc!=0 or y%mdc!=0:
    mdc = mdc - 1
print(mdc)
    
