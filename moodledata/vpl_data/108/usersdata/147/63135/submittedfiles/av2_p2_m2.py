# -*- coding: utf-8 -*-
t=int(input('digite salas:'))
h=[]
for i in range(1,t+1,1):
    por=int(input('porta valor:'))
    h.append(por)
ta=int(input('entrada:'))
ti=int(input('saida:'))
sm=0
for j in range(ta,ti+1,1):
    sm=sm+h[j]
print(sm)