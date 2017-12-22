 -*- coding: utf-8 -*-

v=int(input('digite: '))
t=int(input('digite: '))
for i in range(0,t,1):
    ai=int(input('digite as trocas de volume: '))
    if (v+ ai)>100:
        v=100
    elif (v+ ai)<100:
        v=0
    else:
        v= v+ ai
print(v)        