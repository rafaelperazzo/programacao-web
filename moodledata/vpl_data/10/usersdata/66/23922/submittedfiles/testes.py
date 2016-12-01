# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO
n=input("n:")
cont=0
for i in range(1,n+1,1):
    if i%2==0:
        cont=cont+1
if cont==2:
    print "p"
else:
    print "n"
