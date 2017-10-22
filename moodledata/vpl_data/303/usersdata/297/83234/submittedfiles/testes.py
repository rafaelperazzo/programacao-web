# -*- coding: utf-8 -*-
n=int(input('digite um n: '))
i=1
fat=1
if n>=0 :
    while i<=n :
        fat= 1*i*fat
        i=i+1
    print("%d"%fat)
else: