# -*- coding: utf-8 -*-
a = int(input())
b = int(input())
c = int(input())
ma = 0
mb = 0

while c >= a or c >= b:
    if c >= a:
        ma = ma + 1
        c = c - a
    if c >= a:
        mb = mb + 1
        c = c - b

if c == 0:
    print(ma)
    print(mb) 
else:
    print('N')
