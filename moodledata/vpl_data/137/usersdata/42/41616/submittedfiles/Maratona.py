# -*- coding: utf-8 -*-
n=int(input())
m=int(input())
p1=int(input("digite a distancia do posto 1: "))
pode="S"
for i in range(2,n+1,1):
    p2=int(input("digite a distancia do posto %i: "%i))
    if p2-p1>m:
        pode="N"
    p1=p2
print(pode)