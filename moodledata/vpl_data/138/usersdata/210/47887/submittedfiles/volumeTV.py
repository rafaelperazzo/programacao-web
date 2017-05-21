 -*- coding: utf-8 -*-
 
v=int(input('digite v:'))
t=int(input('digite t:'))
cont=v
for i in range(1,t+1,1):
    a=int(input('digite alteração:'))
    
    if (cont+a)<=100 and cont>=0:
         cont=cont+a
    elif (cont+a)>=100:
        v=cont-100
        cont=cont-v
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 