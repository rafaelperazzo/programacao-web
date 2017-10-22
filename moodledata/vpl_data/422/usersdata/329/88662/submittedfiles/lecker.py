# -*- coding: utf-8 -*-
import math
a = int(input(' '))
b = int(input(' '))
c = int(input(' '))
d = int(input(' '))
while d > c or c > b or b > a:
    print ('S')
    while d < c or c < b or b < a and a == b or b == c or c == d:
        print ('N')
        break
        
  


