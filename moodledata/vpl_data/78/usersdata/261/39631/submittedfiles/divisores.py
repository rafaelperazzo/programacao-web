# -*- coding: utf-8 -*-
import math
def div():
    n = int(input("Qual a quantidade de divisores? "))
    a = int(input("Qual o 1º valor? "))
    b = int(input("Qual o 2º valor? "))
    count=1
    while n>count:
        print (a*count)
        print (b*count)
        count+=1
div()