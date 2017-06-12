# -*- coding: utf-8 -*-
i=1000
p=0
q=0
for i in range(1000,10000,1):
    p=i//100
    q=i%100
    i=i+1
    if (p+q)==(i**(0.5)):
        print(i)
print(p)