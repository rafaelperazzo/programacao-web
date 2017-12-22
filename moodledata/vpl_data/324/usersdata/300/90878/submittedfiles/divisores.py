# -*- coding: utf-8 -*-
import math

n = int(input('Digite a quantidade de múltiplos: '))
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = 0
m = 0
while c < n:
    while m == 0:
            continue
    if m%a == 0 or m%b == 0:
        print(m)
        c = c+1
    m = m+1
    
