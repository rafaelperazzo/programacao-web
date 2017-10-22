
# -*- coding: utf-8 -*-
s=int=0
x=0
A=10000000
while (True) :
    n=int=(input())
    if (n>99999999) :
    
       print('NAO SEI')
    else :   
    
     for  i in range (0,9,1) :    
      x=n//A  
      n=(n-(n//A*A))

      A=A/10
      s=int=(s+x)
    
print('%d'%s) 



















