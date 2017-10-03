# -*- coding: utf-8 -*-
import math

#COMECE SEU CODIGO A

n = int(input( 'Diz ai'))

nota20 = 0
nota10 = 0
nota5 = 0
nota2 = 0
nota1 = 0

while(n>=20):
    n-20
    nota20=nota20+1
    
while(n>=10):
    n-10
    nota10=nota10+1

while(n>=5):
    n-5
    nota5=nota5+1

while(n>=2):
    n-2
    nota2=nota2+1
    
while(n>=1):
    n-1
    nota1=nota1+1
    
print(nota20)
print(nota10)
print(nota5)
print(nota2)
print(nota1)

    
    
    