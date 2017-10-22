# -*- coding: utf-8 -*-
import math
a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))
c = int(input("Terceiro número: "))
i=1
mmc=1
while (i%a!=0) and (i%b!=0) and (i%c!=0):
    if (i%a==0) and (i%b==0) and (i%c==0):
        print(i)
        break
    i=i+1
    
    

