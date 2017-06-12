# -*- coding: utf-8 -*-
i=10000
while i<=9999:
    d1=i%100
    d2=i//10
    if (d1+d2)*(d1+d2)==i:
        print(i)
  