# -*- coding: utf-8 -*-
import math
n=int(input("Digite um valor:"))
n1=int(input("Digite um valor:"))
n2=int(input("Digite um valor:"))
n3=int(input("Digite um valor:"))
x=0
if (n>n1 ):
    x=x+1
    
if (n1>n2 and n1>n):
    x=x+1
    
if (n2>n1 and n2>n3):
    x=x+1
    
if (n3>n2):
    x=x+1
    
    
if (x>=2 or x==0):
    print ("N")
else:
    print ("S")