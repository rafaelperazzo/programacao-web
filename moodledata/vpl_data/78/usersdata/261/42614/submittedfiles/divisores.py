# -*- coding: utf-8 -*-
import math
def mult():
    n = int(input("Qual a quantidade de divisores? "))
    a = int(input("Qual o 1º valor? "))
    b = int(input("Qual o 2º valor? "))
    p =1
    
    while p<n:
        if p%a== 0 or p%b==0:
            mul = p
            print (mul)
        p=p+1


mult()