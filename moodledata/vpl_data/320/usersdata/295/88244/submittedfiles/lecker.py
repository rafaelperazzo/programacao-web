# -*- coding: utf-8 -*-
import math
a = int(input("Digite o primeiro numero :"))
b= int(input("Digite o segundo numero :"))
c = int(input("Digite o terceiro numero :"))
d = int(input("Digite o quarto numero :"))
if (a<b) and (b<c) and (c<d):
    print("S")
elif (a<b) and (c<b) and (d<c):
    print("S") 
elif (b>a) and (c>b) and (c<d):
    print("S")
elif (a>b) and (b>c) and (c>d):
    print("S")
elif (a>b) and (b==c) and (c==d):
    print("S")
elif (a<b) and (b==c) and (c==d):
    print("S")
elif (a==b) and (b<c) and (c==d):
    print("S")
elif (a==b) and (b>c) and (c==d):
    print("S")
elif (a==b) and (b==c) and (c<d):
    print("S")
elif (a<b) and (b==c) and (c<d):
    print("S")
elif (a>b) and (b==c) and (c>d):
    print("S")
elif (a==b) and (b<c) and (c>d):
    print("S")
elif (a>b) and (a==c) and (a==d):
    print("S")
else:
    print("N")