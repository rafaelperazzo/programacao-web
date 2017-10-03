# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
valor= int(input("Digite o valor que deseja sacar:"))

x=valor

if valor >= 20 :
    not20 = valor//20
    x= valor - not20
    print ("%d" %not20 )

else:
    print ("0")
    
if  x >= 10:
    not10=x//10
    x=x-not10
    print ("%d" %not10 )
else:
    print ("0")
if x >= 5:
    not5=x//5
    x=x-not5
    print ("%d" %not5 )
else:
    print ("0")
if x>=2:
    not2=x//2
    k=z-not2
    print ("%d" %not2 )
else: 
    print ("0")
if x>= 1:
    not1=x//1
    print ("%d" %not1 )
        