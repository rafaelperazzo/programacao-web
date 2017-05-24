# -*- coding: utf-8 -*-
import math
p=int(input('Digite o primeiro valor: '))
q=int(input('Digite o segundo valor: '))
k=0
r=1
if p>q:
    while r>0:
        r=p%q
        k=k+1
        p=q
        q=r
        if p%q==0:
            k=k+1
            break
        print(r)
        print(k)
