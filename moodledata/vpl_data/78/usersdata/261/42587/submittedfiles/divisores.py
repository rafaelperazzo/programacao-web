# -*- coding: utf-8 -*-
import math
def div():
    n = int(input("Qual a quantidade de divisores? "))
    a = int(input("Qual o 1º valor? "))
    b = int(input("Qual o 2º valor? "))
    count = 1
    div = 1
    while count<=n:
        if div%a == 0 or div%b == 0:
            print div
            count+=1
            



        
div()