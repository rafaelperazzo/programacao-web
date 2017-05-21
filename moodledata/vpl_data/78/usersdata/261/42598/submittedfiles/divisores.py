# -*- coding: utf-8 -*-
import math
def mult():
    n = int(input("Qual a quantidade de divisores? "))
    a = int(input("Qual o 1º valor? "))
    b = int(input("Qual o 2º valor? "))
    divi = 1
  
    while divi<=n:
        if divi%a == 0 or divi%b == 0:
            print (divi)
            divi+=1
        



        
mult()