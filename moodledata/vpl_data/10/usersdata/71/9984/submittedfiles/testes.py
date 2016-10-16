# -*- coding: utf-8 -*-
from __future__ import division

p=input("Insira p: ")
q=input("Insira q: ")

contp=0
contq=0
ip=1
iq=1

while p//ip!=0:
    contp=contp+1
    ip=ip*10
while q//iq!=0:
    contq=contq+1
    iq=iq*10
    