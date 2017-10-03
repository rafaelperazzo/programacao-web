# -*- coding: utf-8 -*-
#COMECE SEU CÓDIGO AQUI
import math
print("---------------------------------------------------------------")
print("Welcome to my calculus world!!! ;D Enjoy!!!")
print("---------------------------------------------------------------")
cont=1
pi=math.pi
g=9.81
e=0.000002
while cont==1:
    f=float(input("\n\nEnter 'f' value: "))
    L=float(input("Enter 'L' value: "))
    Q=float(input("Enter 'Q' value: "))
    delt_H=float(input("Enter 'DeltaH' value: "))
    O=float(input("Enter 'v' value: "))
    D=((8*f*L*(Q**2))/((pi**2)*g*delt_H))**(1/5)
    Rey=(4*Q)/(pi*D*O)
    k=0.25/((math.log10((e/(3.7*D))+(5.74/(Rey**0.9))))**2)
    print("\nThe D, Rey and k value are, respectively:")
    print("%.4f"%D)
    print("%.4f"%Rey)
    print("%.4f"%k)
    cont=int(input("\n\nDo you wish to continue? (Enter 1 for yes or other number to no): "))
    
    