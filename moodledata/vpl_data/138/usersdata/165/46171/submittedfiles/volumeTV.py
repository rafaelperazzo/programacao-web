 -*- coding: utf-8 -*-
 V=int(input('digite o volume inicial:'))
 T=int(input('digite o numero de trocas:'))
 
 for i in range(1,T+1,1):
     t=int(input('digite t:'))
     a=V+t
     if a>=100:
        a=100
     if a<=0:
        a=0
     else:
        a=a
    
 print(a)        