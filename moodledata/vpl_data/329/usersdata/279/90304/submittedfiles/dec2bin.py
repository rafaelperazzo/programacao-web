# -*- coding: utf-8 -*-
a=10
s=1
t=1
g=0
while (True) :
     p=int(input())     
     if p<0 :
         break
while (True) :
     q=int(input())     
     if q<0 :
         break     
while (True) :
    if q>=a :
       s=s+1
       a=a*10
    else :
        break

while (True) :
    if p>=a :
       t=t+1
       a=a*10
    else :
        break
    
while (True) :
    if (q//(10**(t-1)))==(p//(10**(t-1)))  :
        t=t+1
        g=g+1
        if ((q//(10**(t-1))))==(p//(10**(t-1))) :
         t=t+1
         g=g+1
    if g==2 :
        print ('S')
        break
    else :
        if t==s :
            print('N')
            break
    
    
    
    
    
    
    
    
    
    