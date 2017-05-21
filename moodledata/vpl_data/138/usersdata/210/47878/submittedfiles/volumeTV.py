 -*- coding: utf-8 -*-
 
 v=int(input('digite v :'))
 f=int(input('digite f:'))
 cont=v
 for i in range(1,f+1,1):
     a=int(input('digite alteração:'))
    
     if (cont+a)<=100 and cont>=0:
         cont=cont+a
     elif (cont+a)>=100:
         e=cont-100
         cont=cont-v
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 