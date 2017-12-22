# -*- coding: utf-8 -*-
import math
n = int(input("Insira a quantidade de multiplos: ")) 
a = int(input("Qual o numero de a?: "))
b = int(input("QUal o numero de b?: "))
numeroteste=1
cont=0
while(cont<n):
    if (numeroteste%a)==0 or (numeroteste%b)==0:
        print(numeroteste)
        numeroteste=numeroteste+1
        cont=cont+1
    else:
        numeroteste=numeroteste+1