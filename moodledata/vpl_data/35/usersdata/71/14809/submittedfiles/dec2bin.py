# -*- coding: utf-8 -*-
from __future__ import division

p = input("p: ")
q = input("q: ")

contp=0
ip=1
contador=0   

while p//ip!=0:
    contp=contp+1
    ip=ip*10

while q>1:
    if q%(10**contp)==p:
        contador=contador+1
        break
    else:
        q=q//10

if contador==1:
    print "S"
else:
    print "N"