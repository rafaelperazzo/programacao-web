# -*- coding: utf-8 -*-
a= float(input('Digite o valor de a:'))
b= float(input('Digite o valor de b:'))
c= float(input('Digite o valor de c:'))

if (a>b) and (b>c):
   print(c)
   print(b)
   print(a)
   
elif (c>b) and (b>a):
   print(a)
   print(b)
   print(c)
   
elif (b>a) and (a>c):
   print(c)
   print(a)
   print(b)

elif (b>c) and (c>a):
   print(a)
   print(c)
   print(b)
   
elif (a>c) and (c>b):
   print(b)
   print(c)
   print(a)
   
else: 
   print(b)
   print(a)
   print(c)
   