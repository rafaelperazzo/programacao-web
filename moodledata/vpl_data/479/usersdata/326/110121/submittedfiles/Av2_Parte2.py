# -*- coding: utf-8 -*-
import math
a = int(input('Digite a: '))
b = int(input('Digite b: '))

while a <= 0:
    a = int(input('Digite a: '))
while b <= 0:
    b = int(input('Digite b: '))

def mdc(a,b):
    while a//2 == 0 and b//2== 0:
        mdc = a/2 and b/2
        