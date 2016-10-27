# -*- coding: utf-8 -*-
from __future__ import division
p=input("digiete p:")
q=input("digite q:")
cont=0
a = p
while p>0:
    p=p//10
    cont=cont+1
p = a
while q>0:
    ultimos=q%(10**cont)
    if ultimos==p:
        print ("S")
        break
    else:
        q=q//10
