# -*- coding: utf-8 -*-
from __future__ import division

p = int(input('Digite o valor de p :'))
q = int(input('Digite o valor de q :'))

dp = 0
i = p
while i >= 1:
    dp = dp +1
    i = i//10
    
subn = 0
while q > 0:
    if q%(10**dp) == p:
        subn = subn +1
        break
    q = q//10

if subn > 0 :
    print('S')
else:
    print('N')