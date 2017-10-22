# -*- coding: utf-8 -*-
import math
n1=int(input("Digite um numero n1: "))
n2=int(input("Digite um numero n2: "))
n3=int(input("Digite um numero n3: "))
n4=int(input("Digite um numero n4: "))
while (True):
    if n1>n2 and n2!=n3!=n4 or n1<n2>n3 and n1!=n4!=n3 or n2<n3>n4 and n2!=n1!=n4 or n3<n4 and n1!=n2!=n4:
        print ("S")
    else:
        print ("N")