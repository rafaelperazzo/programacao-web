
# -*- coding: utf-8 -*-

while (True) :
    s=0
    x=0
    A=10000000
    n=int=(input())
    if n<=99999999 and n>=10000000 :
        break
        print('NAO SEI')
    else :   
    
      for  i in range (0,9,1) :    
       x=n//A  
       n=(n-(n//A*A))

       A=A/10
       s=int=(s+x)
      break
print('%d'%s) 



















