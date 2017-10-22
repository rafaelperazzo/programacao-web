# -*- coding: utf-8 -*-
import math
n1=int(input("Primeiro Número: "))
n2=int(input("Segundo Número: "))
if ni>=n2:
    use=n2
if ni<n2:
    use=n1
for i in range (use,1,1):
    if ni%i == 0 and n2%i == 0:
        print (i)
        break
