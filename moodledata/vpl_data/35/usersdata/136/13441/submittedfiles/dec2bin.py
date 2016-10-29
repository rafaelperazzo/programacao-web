# -*- coding: utf-8 -*-
from __future__ import division

p = input("Digite o valor de p:")
q = input("Digite o valor de q:")
cont = 0
i = p
while p>0:
    p = p//10
    cont = cont + 1
p = i
sub = 0
while q>0:
    last = q%(10**cont)
    if last == p:
        sub = sub + 1
        break
    else:
        q = q//10
if sub == 0:
    print("N")
else:
    print("S")