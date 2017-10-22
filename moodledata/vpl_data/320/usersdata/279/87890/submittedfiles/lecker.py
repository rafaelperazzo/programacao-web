# -*- coding: utf-8 -*-
import math

a1=float(input())
a2=float(input())
a3=float(input())
a4=float(input()) 
r=0

if a1>a2 and a1>a3 and a1>a4 :
      r=r+1
if a2>a3 and a2>a1 and a2>a4 :
      r=r+1  
if a3>a2 and a3>a1 and a3>a4 : 
      r=r+1
if a4>a3 and a4>a1 and a4>a2 :
      r=r+1
if r>1 or r==0 :
    print('N')
else :
    print('S')