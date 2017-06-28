# -*- coding: utf-8 -*-
def degrau(h):
    d=[]
    for i in range(0,len(h),1):
        c=h[i]-h[i+1]
        if c<0:
            c=c