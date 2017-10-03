# -*- coding: utf-8 -*-
import math
n=int(input('Digite o valor de n: '))
nume=1
deno=n
s=0
while(nume<n) and (deno>=1):
    s=s+nume/deno
    nume=nume+1
    deno=deno-1
print(s)
    


