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
    if a<b or or b>c or c>d or d>a:
        print('S')
    elif a<b and c<d or b<c and d<a or a==b==c==d:
        print('N')
    
        
        
