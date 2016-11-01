# -*- coding: utf-8 -*-
from __future__ import division
p=input('Digite p: ')
q=input('Digite q: ')
cont=1
while p/10>1 :
    cont=cont+1
i=10**cont
while q>=p:
    r=q%i
    if r==p:
        print('S')
    else:
        q=q//10
if r==0:
    print('N')
     