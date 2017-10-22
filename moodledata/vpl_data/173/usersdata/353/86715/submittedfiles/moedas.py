# -*- coding: utf-8 -*-
a = int(input())
b = int(input())
c = int(input())
ma = 0
mb = 0
i = c%a
j = c%b


ma = c//a
c = c%a
mb = c//b
c = c%b

if c == 0:
    print(ma)
    print(mb) 
else:
    print('N')
