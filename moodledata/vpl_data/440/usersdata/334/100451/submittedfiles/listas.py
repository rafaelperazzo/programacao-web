# -*- coding: utf-8 -*-

def pico (a):
    m = 0
    for i in range (len(a)-1,1):
        altura = abs(a[i]-abs(a[i+1])
        if abs(altura) > m:
            m = abs(altura)
    return m

n = int(input())
l = []
for i in range (0,n,1):
    l.append(int(input()))

print(comp(l))