# -*- coding: utf-8 -*-
a=float(input(''))      
b=float(input(''))
c=float(input(''))
if a>b and a>c and b>c:
   print('%d'%c)
   print('%d'%b)
   print('%d'%a) 
if b>a and b>c and a>c:
   print('%d'%c)
   print('%d'%a)
   print('%d'%b) 
if c>a and c>b and b>a:
   print('%d'%a) 
   print('%d'%b)
   print('%d'%c)
if a>c and c>b and a>b:
   print('%d'%b) 
   print('%d'%c)
   print('%d'%a)
if b>a and b>c and c>a:
   print('%d'%a)
   print('%d'%c)
   print('%d'%b)
if c>a and c>b and a>b:
   print('%d'%b) 
   print('%d'%a)
   print('%d'%c)