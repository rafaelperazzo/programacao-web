# -*- coding: utf-8 -*-
v=float(input('digite v:'))
t=float(input('digite t:'))
for i in range (1,11,1):
    v=v+(v**t)
    print ('%.2f' %v)