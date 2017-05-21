# -*- coding: utf-8 -*-
import math
n=int(input("Digite n: "))
a=int(input("Digite a: "))
b=int(input("Digite b: "))
cont=0 
cm=1
while cont < n:
    if cm%a==0 or cm%b==0:
        print(cm)
        cont += 1
    cm += 1