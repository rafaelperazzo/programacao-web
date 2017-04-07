# -*- coding: utf-8 -*-
a=float(input('digite a'))      
b=float(input('digite b'))
c=float(input('digite c'))
if a>b and a>c and b>c:
   print('%f'%a)
   print('%f'%b)
   print('%f'%c) 
if b>a and b>c and a>c:
   print('%f'%b)
   print('%f'%a)
   print('%f'%c) 
if c>a and c>b and b>a:
   print('%f'%c) 
   print('%f'%b)
   print('%f'%a)
