# -*- coding: utf-8 -*-
import math
n=int(input("Digite um valor:"))
n1=int(input("Digite um valor:"))
n2=int(input("Digite um valor:"))
n3=int(input("Digite um valor:"))

if (n>n1 and n!=n1):
    print ("S")
elif (n1>n2 or n1>n):
        print ("S")
elif (n2>n1 or n2>n3):
        print ("S")
elif (n3>n2):
        print ("S")
else :
    print("N")
    