# -*- coding: utf-8 -*-
from math import sqrt
print("-----------------------------------------------------------")
print("Welcome to my calculus world!!! Enjoy!!!")
print("-----------------------------------------------------------")
cont=1
while cont==1:
    a=float(input("\n\nEnter the coefficient 'a' value of the second degree equation in the format ax²+bx+c=0 to calculate your roots: "))
    b=float(input("Enter the coefficient 'b' value: "))
    c=float(input("Now enter the coefficient 'c' value: "))
    Delta=(b**2)-4*a*c
    if Delta>=0:
        x1=(-b+sqrt(Delta))/(2*a)
        x2=(-b-sqrt(Delta))/(2*a)
        print("%.2f"%x1)
        print("%.2f"%x2)
    else:
        print("SRR")
    
