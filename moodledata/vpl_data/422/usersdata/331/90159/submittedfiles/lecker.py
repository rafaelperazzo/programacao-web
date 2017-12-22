# -*- coding: utf-8 -*-
import math
a = int(input('digite um numero:'))
b = int(input('digite um numero:'))
c = int(input('digite um numero:'))
d = int(input('digite um numero:'))
if b>a and d>c:
    print ('N')
elif a>b:
    print ('S')
elif b>a:
    print ('S')
elif b>c:
    print ('S')
elif c>b:
    print ('S')
elif c>d:
    print ('S')
elif d>c:
    print ('S')
else:
    print('N')



#else :
  #  print ('N')
   # if a==300 and b==300 and c==300 and d==300:
    #    print ('N')
    #else:
     #   print ('S')