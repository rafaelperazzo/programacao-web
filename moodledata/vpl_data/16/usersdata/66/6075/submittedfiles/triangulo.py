# -*- coding: utf-8 -*-
from __future__ import division
import math
A=int(input("digite a:"))
B=int(input("digite b:"))
C=int(input("digite c:"))
if A<(B+C):
    print("s")
    if (A)**2==((B)**2 +(C)**2):
        print("Re")
    if (A)**2>((B)**2 + (C)**2):
        print("Ob")
    if (A)**2==((B)**2 + (C)**2):
        print("Ac")
    if A==B==C :
        print("Eq")
        if B==C!=A :
            print("Is")
            if A!=B!=C :
                print("Es")
        
        
else:
    print("N")
