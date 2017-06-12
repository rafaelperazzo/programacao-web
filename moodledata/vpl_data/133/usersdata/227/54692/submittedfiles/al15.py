# -*- coding: utf-8 -*-
i=1000
while(i<=9999):
    
    n1=i//100
    n2=i%100
    if (n1+n2)*(n1+n2)==i:
        print(i)
    i=i+1    
    
    