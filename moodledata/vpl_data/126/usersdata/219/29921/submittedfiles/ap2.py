# -*- coding: utf-8 -*-
a=int(input('Digite a :'))
b=int(input('Digite b :'))
c=int(input('Digite c :'))
d=int(input('Digite d :'))
if a>=b and a>=c and a>=d:
    print(a)
    if b<=c and b<=d:
        print(b)
    elif c<=b and c<=d:
        print(c)
    else:
        print(d)
if b>=a and b>=c and b>=d:
    print(b)
    if a<=c and a<=d:
        print(a)
    elif c<=a and c<=d:
            print(c)
    else:
            print(d)
if c>=a and c>=b and c>=d:
    print(c)
    if a<=b and a<=d:
        print(a)
    elif b<=a and b<=d:
        print(b)
    else:
        print(d)
if d>=a and d>=b and d>=c:
   print(d)
   if a<=b and a<=c:
      print(a)
   elif b<=a and b<=c:
        print(b)
   else:
       print(c)
            
    
    
    
