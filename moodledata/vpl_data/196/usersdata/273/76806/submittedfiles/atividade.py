# -*- coding: utf-8 -*-
import math
n=int(input('Digite o valor de n: '))
nume=1
deno=n
s=0
i=1
while(nume<=n) and (deno>=1):
    s=s+nume/deno
    nume=nume+i
    deno=deno-i
i=i+1
print(s)
    


