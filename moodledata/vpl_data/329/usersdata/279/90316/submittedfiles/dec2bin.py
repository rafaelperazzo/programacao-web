# -*- coding: utf-8 -*-
a=10
s=1
t=1
g=0
while (True) :
     p=(int(input())) 
     if (p>=0) :
        break
while (True) :
     q=(int(input()))     
     if (q>=0) :
        break     
while (True) :
    if (q>=a) :
       s=s+1
       a=a*10
    else :
        break

while (True) :
    if (p>=a) :
       t=t+1
       a=a*10
    else :
        break
b=t    
while (True) :
    
    if ((q//(10**(b-1)))==(p//(10**(b-1))))  :
        b=b+1
        g=g+1
        
    if (g==t) :
        print ('S')
        break
    else :
        if (t==s) :
            print('N')
            break
    
    
    
    
    
    
    
    
    
    