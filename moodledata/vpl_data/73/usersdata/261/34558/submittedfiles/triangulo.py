# -*- coding: utf-8 -*-
import math
def triangulo():
    a=float(input("Qual o comprimento do 1º lado? "))
    b=float(input("Qual o comprimento do 2º lado? "))
    c=float(input("Qual o comprimento do 3º lado? "))
    if not a<b+c:
        print ("N")
    elif a<b+c:
        print ("S")
        a=a1
        b=b1
        c=c1
        
    if (a1**2)==(b1**2)+(c1**2):
        print ("Re")
    elif (a1**2)>(b1**2)+(c1**2):
        print ("Ob")
    elif (a1**2)<(b1**2)+(c1**2):
        print ("Ac")
        
    if a1==b1 and b1==c1:
        print ("Eq")
    elif b1==c1 and c1!=a1:
        print ("Is")
    elif a1!=b1 and b1!=c1 and a1!=c1:
        print ("Es")
    
    
triangulo()