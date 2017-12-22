# -*- coding: utf-8 -*-
import math

n1=int(input('Digite n1: '))
n2=int(input('Digite n2: '))
n3=int(input('Digite n3: '))
n4=int(input('Digite n4: '))
cont=0
if n1>n2:
    cont=cont+1
if n2>n1 and n2>n3:
    cont=cont+1
if n3>n2 and n3>n4:
    cont=cont+1
if n4>n3:
    cont=cont+1
if cont==1:
    print("'S'")
else:
    print("'N'")
    

  