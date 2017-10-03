# -*- coding: utf-8 -*-
n = int(input('Digite o valor de n: '))
i = 1
fat = 1
while (i<=n) :
    fat2 = i*fat
    fat = fat2
    i=i+1
print(fat2)