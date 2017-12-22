# -*- coding: utf-8 -*-

n=(int(input()))
if n<3 :
    print('N')
else :    
 lista=[]
 c=0
 e=0
 r=0
 for i in range (0,n,1) :
   lista.append(int(input()))
 for i in range (0,n-1,1) :  
   if lista[i] < lista[i+1] :
      c+=1
      r=(i+1)
         
     
   if lista[i] == lista[i+1] :
        print ('N')
        r=(i+1)
        break
      
   if lista[i] > lista [i+1] :
       d+=1
       s=(i+1)
if c==r and  (s-d)==r :
    print ('S')
else :
    print('N')







































































