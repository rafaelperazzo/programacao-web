# -*- coding: utf-8 -*-
n1=float(input('digite n1'))
n2=float(input('digite n2'))
n3=float(input('digite n3'))
if n1 < n2 and n2 < n3:
    print (n1)
    print (n2)
    print (n3)
elif n2 < n1 and n1 < n3:
    print (n2)
    print (n1)
    print (n3)
elif n3 < n1 and n1 < n2:
    print (n3)
    print (n1)
    print (n2)
elif n2 < n3 and n3 < n1:
    print (n2)
    print (n3)
    print (n1)
elif n1 > n3 and n3 > n2:
    print (n1)
    print (n3)
    print (n2)
elif n3 > n2 and n2 > n1:
    print (n3)
    print (n2)
    print (n1)
else:
    print('cu')
    