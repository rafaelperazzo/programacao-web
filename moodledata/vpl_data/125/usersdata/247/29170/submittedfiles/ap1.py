# -*- coding: utf-8 -*-
a=float(input('digite a'))      
b=float(input('digite b'))
c=float(input('digite c'))
if a>b and a>c and b>c:
   print('%f'%c)
   print('%f'%b)
   print('%f'%a) 
if b>a and b>c and a>c:
   print('%f'%c)
   print('%f'%a)
   print('%f'%b) 
if c>a and c>b and b>a:
   print('%f'%a) 
   print('%f'%b)
   print('%f'%c)
if a>c and c>b and a>b:
   print('%f'%b) 
   print('%f'%c)
   print('%f'%a)
if b>a and b>c and c>a:
   print('%f'%a)
   print('%f'%c)
   print('%f'%b)
if c>a and c>b and a>b:
   print('%f'%b) 
   print('%f'%a)
   print('%f'%c)