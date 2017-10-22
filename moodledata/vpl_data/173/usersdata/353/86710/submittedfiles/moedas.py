# -*- coding: utf-8 -*-
a = int(input())
b = int(input())
c = int(input())
ma = 0
mb = 0
i = c%a
j = c%b

if i%b == 0 or j%a == 0:
    ma = c/a
    c = c%a
    mb = c/b
    print(ma)
    print(mb)
else:
    print('N')
