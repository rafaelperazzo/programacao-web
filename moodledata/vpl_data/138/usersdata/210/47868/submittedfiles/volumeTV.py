 -*- coding: utf-8 -*-
 E=int(input('digite E:'))
 F=int(input('digite F:'))
 cont=E
 for i in range(1,F+1,1):
     A=int(input('digite alteração:'))
     if (cont+A)<=100 and cont>=0:
         cont=cont+A
     elif (cont+A)>=100:
         E=cont-100
         cont=cont-E
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 