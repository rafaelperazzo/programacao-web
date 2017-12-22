# -*- coding: utf-8 -*-
M = int(input())
while M<2 or M>1000:
    M = int(input())

N = int(input())
while N<2 or N>1000:
    N = int(input())

quadras = []
for i in range (0,N,1):
    ruas = []
    for j in range (0,M,1):
        a = (int(input()))
        while a<1 or a>100:
            a = (int(input()))
            ruas.append(a)

for j in range (0,M,1)
    sum(quadras[i][j])