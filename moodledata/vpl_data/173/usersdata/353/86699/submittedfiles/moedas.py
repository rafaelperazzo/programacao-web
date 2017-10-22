# -*- coding: utf-8 -*-
a = int(input())
b = int(input())
c = int(input())
ma = 0
mb = 0

if c%a == 0 or c%b == 0:
ma = c//a
c = a%c
    if a%c == 0:
        break
mb = c//b
print(a)
print(b)
else:
    print('N')
