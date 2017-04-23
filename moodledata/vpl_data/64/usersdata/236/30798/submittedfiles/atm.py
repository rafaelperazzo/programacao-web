# -*- coding: utf-8 -*-
from __future__ import division
import math

VALOR= int(input('Digite o valor que deseja sacar:')

a= VALOR // 20
b= VALOR //10
c= VALOR //5
d= VALOR //2
e= VALOR //1
R= VALOR - ((a*20)+(b*10)+(c*5)+(d*2))
R2= VALOR - ((a*20)+(b*10)+(c*5))
if a=0 and b=0 and c=0 and d=0 and e=1:
    print('%d,%d,%d,%d,%d'%(a,b,c,d,e))

if a=0 and b=0 and c=0 and d=0 or d!=0:
    print('%d,%d,%d,%d,%d'%(a,b,c,d,R))
    
if a=0 and b=0 and c=1 and VALOR=5:
    print('%d,%d,%d,0,0'%(a,b,c))
    
if a=0 and b=0 and c=1 and d%2=0:
    print('%d,%d,%d,%d,%d'%(a,b,c,0,R2))
    




    
    
    


