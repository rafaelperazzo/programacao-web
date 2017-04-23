# -*- coding: utf-8 -*-
import math
def lecker():
    a = float(input("Qual o 1º número? "))
    b = float(input("Qual o 2º número? "))
    c = float(input("Qual o 3º número? "))
    d = float(input("Qual o 4º número? "))
    if a>b and (b>=c or b<c) and c>=d: #maior apenas a
        print ("S")
    elif a<b and b>c and c>=d: #maior apenas b
        print ("S")
    elif a<=b and b<c and c>d: #maior apenas c
        print ("S")
    elif a<=b and (b<=c or b>c)and c<d: #maior apenas d
        print ("S")
    else:
        print("N")
    

    

lecker()