# -*- coding: utf-8 -*-
i=1000
while i<=9999:
    a1=i%100
    a2=i/100
    if (a1+a2)*(a1+a2)==i:
print(i)
i=i+1
