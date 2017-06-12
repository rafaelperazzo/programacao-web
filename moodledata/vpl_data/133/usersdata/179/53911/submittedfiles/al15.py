# -*- coding: utf-8 -*-
for i in range(1000,9999,1):
    raiz=(i**1/2)
    DI=i//100
    w=DI+(i-DI*100)
    if raiz==w:
        print(i)
        