# -*- coding: utf-8 -*-
from __future__ import division

p=input("Digite o valor do primeiro número:")
q=input("Digite o valor do segundo número:")
cont=1
while (q//10!=0):
    if q//10!=0:
        cont=cont+1
    q=q//10
    
for i in range (1,cont+1,1):
    if q//10==p:
        print("S")
    q=q//10


    