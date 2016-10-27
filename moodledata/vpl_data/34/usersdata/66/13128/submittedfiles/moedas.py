# -*- coding: utf-8 -*-
from __future__ import division
a=int(input("digite a:"))
b=int(input("digite b:"))
c=int(input("digite c:"))
qa=c//a
qb=0
while qa>0:
    t=c-(qa*a)
    if t%b==0:
        qb=t//b
        break
    else:
        qa=qa-1
        
        
qb=c//
qa=0
while qb>0:
    t=c-(qb*b)
    if t%a==0:
        qa=t//a
        break
    else:
        qb=qb-1
        
        
        
        
        
        

if qa and qb ==0:
    print "N"
else:
    print qa
    print qb