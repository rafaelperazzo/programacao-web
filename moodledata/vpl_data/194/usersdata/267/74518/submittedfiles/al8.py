# -*- coding: utf-8 -*-
n=int(input('Número: '))
fat=n
while n>1:
    fat=fat*(n-1)
    n=n-1
print(fat)