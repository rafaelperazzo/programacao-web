# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
def atm():
    v = int(input("Quanto você deseja sacar? "))
 
    p20 = v//20
    if p20 > 0:
        r20 = v%p20
    elif p20 == 0:
        r20 = v
 
    p10 = r20//10
    if p10 > 0:
        r10 = r20%p10
    elif p10 == 0:
        r10 = r20
 
    p5  = r10//5
    if p5 > 0:
        r5 = r10%p5
    elif p5 == 0:
        r5 = r10
        
    p2  = r5//2
    if p2>0:
        r2 = r5%p2
    elif p2 == 0:
        r2 = r5
 
    p1  = r2
    
    print (p20)
    print (p10)
    print (p5)
    print (p2)
    print (p1)

atm()