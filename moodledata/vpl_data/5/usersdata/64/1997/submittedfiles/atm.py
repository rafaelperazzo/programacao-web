# -*- coding: utf-8 -*-
from __future__ import division
import math

#ENTRADA

v = int(input('Digite a quantidade a ser sacada: '))
d20 = 0
d10 = 0
d5 = 0
d2 = 0
d1 = 0

#PROCESSAMENTO]

while v >=20:
    d20 = d20 + 1
    
    v = v - 20
    
while v >= 10 < 20:
    d10 = d10 + 1
        
    v = v - 10
        
while v >= 5 < 10:
    d5 = d5 + 1
            
    v = v - 5
            
while v >= 2 < 5:
    d2 = d2 + 1
                
    v = v -2
                
while v >=1 <2:
    d1 = d1 + 1
                    
    v = v - 1
                    
#SAÍDA

print str(d20)
print str(d10)
print str(d5)
print str(d2)
print str(d1)


