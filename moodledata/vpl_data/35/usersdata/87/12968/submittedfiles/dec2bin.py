# -*- coding: utf-8 -*-
from __future__ import division

p = int(input("Digite valor de p: "))
q = int(input("Digite valor de q: "))

i=1
while i<=p:
    i=i*10
while q>=p:
    s=q%10
    q=q/10
if s==p:
    print("S")
else:
    print("N")