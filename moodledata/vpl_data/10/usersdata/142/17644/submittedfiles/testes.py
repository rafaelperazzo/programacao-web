# -*- coding: utf-8 -*-
from __future__ import division

a=[1,2,3,4,5,6]
b=[1,2,3]

cont=0
for x in range(0,len(b),1):
    for i in range(0,len(a),1):
        if a[i]==b[x]:
            cont=cont+1
print cont