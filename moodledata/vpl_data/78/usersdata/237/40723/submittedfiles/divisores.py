# -*- coding: utf-8 -*-
import math
n=int(input("Digite n: "))
a=int(input("Digite a: "))
b=int(input("Digite b: "))
x=0
h=0
while x>= 0 :
    if x%a == 0 or x%b == 0:
        print(x)
        x=x+1
        h=h+1
    if h==n:
        break
    
        

    

