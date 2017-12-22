# -*- coding: utf-8 -*-
p1 = 80000
t1 = 3/100
p2 = 200000
t2 = 15/1000
crescimento_p1 = p1*t1
crescimento_p2 = p2*t2
while p1<p2:
    crescimento_pop= crescimento_p1*t1
    if crescimento_pop==crescimento_p2:
        break
    