# -*- coding: utf-8 -*-
import math
def mult():
    n = int(input("Qual a quantidade de divisores? "))
    a = int(input("Qual o 1º valor? "))
    b = int(input("Qual o 2º valor? "))
    p = 1
    c = 1
    while 1:
        if p%a== 0 or p%b==0:
            print (p)
            c+=1
        p=p+1
        if c==n+1:
            break


mult()