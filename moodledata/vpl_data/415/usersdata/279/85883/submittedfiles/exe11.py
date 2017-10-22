
# -*- coding: utf-8 -*-

while (True) :
    s=int=0
    x=0
    A=int=10000000
    n=int=(input())
    if n<=(A*10-1)and n>=A :
        break
        print('NAO SEI')
    else :   
    
      for  i in range (0,9,1) :    
       x=n//A  
       n=(n-(n//A*A))

       A=A/10
       s=int=(s+x)
    
print('%d'%s) 



















