# -*- coding: utf-8 -*-
import math
n = int(input("Digite a quantidade de números a serem mostrados: "))
a = int(input("Digite o número 1: "))
b = int(input("Digite o número 2: "))
i=2
x=2
if a>b:
    while (n>0):
        while (i<=a):
            if a%i==0 or b%i==0:
                print(i)
                n-=1
                i+=1
        print(b*x)
        n-=1
        print(a*x)
        n-=1
        x+=1
if b>a:
    while (n>0):
        while (i<=b):
            if a%i==0 or b%i==0:
                print(i)
                n-=1
                i+=1
