# -*- coding: utf-8 -*-
import math
def angulo():
    if (a**2)==(b**2)+(c**2):
        print ("Re")
    elif (a**2)>(b**2)+(c**2):
        print ("Ob")
    elif (a**2)<(b**2)+(c**2):
        print ("Ac")

def lado():
    if a==b and b==c:
        print ("Eq")
    elif b==c and c!=a:
        print ("Is")
    elif a!=b and b!=c and a!=c:
        print ("Es")
    


def triangulo():
    a=float(input("Qual o comprimento do 1º lado? "))
    b=float(input("Qual o comprimento do 2º lado? "))
    c=float(input("Qual o comprimento do 3º lado? "))
    if not a<b+c:
        print ("N")
    elif a<b+c:
        print ("S")
        angulo()
        lado()

    
    
triangulo()