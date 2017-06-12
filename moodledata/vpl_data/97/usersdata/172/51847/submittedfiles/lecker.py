# -*- coding: utf-8 -*-
from __future__ import division
def lecker(l):
    c=0
    for i in range(0,len(l),1):
        if i==0:
            if l[i]>l[i+1]:
                c=c+1
        elif i==len(l)-1:
            if l[i]>l[i-1]:
                c=c+1
        else:
            if l[i]>l[i+1] and l[i]>l[i-1]:
                c=c+1
    if cont==1:
        return True
    else:
        return False
    
