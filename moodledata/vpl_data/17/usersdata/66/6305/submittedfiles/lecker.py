# -*- coding: utf-8 -*-
from __future__ import division
import math
A=input("digite a:")
B=input("digite b:")
C=input("digite c:")
D=input("digite d")
if A>B>C>D :
    print("S")
if D>B>C>A :
    print("S")
if C>B and C>D :
    print("S")
if B>C and B>A :
    print("S")
    
else:
    print("N")