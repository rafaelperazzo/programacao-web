# -*- coding: utf-8 -*-
import math

x1 = int(input('Digite x1: '))
x2 = int(input('Digite x2: '))
x3 = int(input('Digite x3: '))
x4 = int(input('Digite x4: '))
x5 = int(input('Digite x5: '))
x6 = int(input('Digite x6: '))
x7 = int(input('Digite x7: '))
x8 = int(input('Digite x8: '))
x9 = int(input('Digite x9: '))

a1 = (x1==1 and x2==1 and x3==1)
b1 = (x4==1 and x5==1 and x6==1)
c1 = (x7==1 and x8==1 and x9==1)
d1 = (x1==1 and x4==1 and x7==1)
e1 = (x2==1 and x5==1 and x8==1)
f1 = (x3==1 and x6==1 and x9==1)
g1 = (x1==1 and x5==1 and x9==1)
h1 = (x3==1 and x5==1 and x7==1)

a2 = (x1==0 and x2==0 and x3==0)
b2 = (x4==0 and x5==0 and x6==0)
c2 = (x7==0 and x8==0 and x9==0)
d2 = (x1==0 and x4==0 and x7==0)
e2 = (x2==0 and x5==0 and x8==0)
f2 = (x3==0 and x6==0 and x9==0)
g2 = (x1==0 and x5==0 and x9==0)
h2 = (x3==0 and x5==0 and x7==0)

#CONTINUE...
if a1 or b1 or c1 or d1 or e1 or f1 or g1 or h1:
    print ("1")
elif a2 or b2 or c2 or d2 or e2 or f2 or g2 or h2:
    print ("0")
else:
    print ("E")
