# -*- coding: utf-8 -*-
import math
n=int(input("Digite n: "))
a=int(input("Digite i: "))
b=int(input("Digite j: "))
cont=0 
cm=0 
while cont < n:
    if cm%a==0 or cm%b==0:
        print(cm)
        cont = 1
    cm = 1