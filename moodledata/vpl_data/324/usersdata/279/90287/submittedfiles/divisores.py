# -*- coding: utf-8 -*-
import math

t=0
while (True) :
     n=(int(input()))
     if n>0 :
         break
while (True) :
     a=(int(input()))
     if a>0 :
         break
while (True) :
     b=(int(input()))
     if b>0 :
         break

while (True) :
    
    s=1
    
    if (s%a)==0 or (s%b)==0 :
        s=s+1
        t=t+1  
        print(s)
        if t==n :
            break
    
    








