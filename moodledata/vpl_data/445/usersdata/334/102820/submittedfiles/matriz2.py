# -*- coding: utf-8 -*-

n = int(input())

m = []

for i in range (0,n-1,1):
    l = []
    for j in range (0,n-1,1):
        l.append(int(input()))
    m.append(l)

print (m)