# -*- coding: utf-8 -*-
decimal=int(input('digite: '))
b=decimal
a=0
while b>0:
    b=b//10
    a=a+1
    
a=a-(a-1) 
numero=0
while decimal > 0:
    resto=decimal%2
    decimal=decimal//2
    numero=resto*(10**a) + numero
    a=a+1
numero=numero//10    
print(numero)
    
    

