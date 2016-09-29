# -*- coding: utf-8 -*-
from __future__ import division
import math 

a = input()
b = input()
da2 = 0
da3 = 0
da5 = 0
da7 = 0
db2 = 0
db3 = 0
db5 = 0
db7 = 0
#primeirotermo
while True:
    if a%2==0:
        a=a/2
        da2=da2+1
    else:
        break
    
while True:
    if a%3==0:
        a=a/3
        da3=da3+1
    else:
        break
    
while True:
    if a%5==0:
        a=a/5
        da5=da5+1
    else:
        break
    
while True:
    if a%7==0:
        a=a/7
        da7=da7+1
    else:
        break
#segundotermo
while True:
    if b%2==0:
        b=b/2
        db2=db2+1
    else:
        break
while True:
    if b%3==0:
        b=b/3
        db3=db3+1
    else:
        break
while True:
    if b%5==0:
        b=b/5
        db5=db5+1
    else:
        break
while True:
    if b%7==0:
        b=b/7
        db7=db7+1
    else:
        break 
#m2357
if da2==0 or db2==0:
    m2=1
elif da2<=db2:
    m2=da2*2
else:
    m2=db2*2
    
if da3==0 or db3==0:
    m3=1
elif da3<=db3:
    m3=da3*3
else:
    m3=db3*3    

if da5==0 or db5==0:
    m5=1
elif da5<=db5:
    m5=da5*5
else:
    m5=db5*5  
    
if da7==0 or db7==0:
    m7=1
elif da7<=db7:
    m7=da7*7
else:
    m7=db7*7
    
#MDC
mdc=m2*m3*m5*m7
print mdc