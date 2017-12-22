# -*- coding: utf-8 -*-
import math
i = 1
a = int(input('digite um numero:'))
b= int(input('digite um numero:'))
c = int(input('digite um numero:'))
d= int(input('digite um numero:'))
if a>b:
    a=300
elif b>a and b>c:
    b=300
elif c>b and c>d:
    c=300
elif d>c:
    d=300
elif a+b+c+d==600:
    print ('N')
#else:
    print ('S')





#else :
  #  print ('N')
   # if a==300 and b==300 and c==300 and d==300:
    #    print ('N')
    #else:
     #   print ('S')