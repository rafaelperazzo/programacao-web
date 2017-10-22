# -*- coding: utf-8 -*-
binario=int(input('digite: '))
b=binario
a=0
while b>0:
    binario=binario//10
    a=a+1
    
a=a-1   
numero=0
while binario//2 > 0:
    resto=binario%2
    binario=binario//2
    numero=resto*(10**a) + numero
    a=a-1
    
    

