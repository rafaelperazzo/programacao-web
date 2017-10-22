# -*- coding: utf-8 -*-
import math
n = int(input('Digine n: '))
a = int(input('Digine a: '))
b = int(input('Digine b: '))

while i <= n+1:
    if i%a != 0 and i%b != 0:
        n = n+1
    if i%a == 0 or i%b == 0:
        print(i)
    i = i + 1
