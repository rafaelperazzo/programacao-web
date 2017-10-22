# -*- coding: utf-8 -*-
import math
#a = int(input(' '))
#b = int(input(' '))
#c = int(input(' '))
#d = int(input(' '))
#while a<b or a>d or b>c or b<a or c>d or c<b or d>a or d<a:
 #   print ('S')
  #  break
#while a>b>c>d or a==b==c==d:
 #   print ('N')
#  break
for i in range(0,4,1):
    a = int(input(' '))  
    b = int(input(' '))
    c = int(input(' '))
    d= int(input(' '))
    if b>a and b>c and d>a and d>c:
        print('N')
    elif a>b>c>d or a==b==c==d:
        print('N')
    else :
        print('S')
    
        
        
