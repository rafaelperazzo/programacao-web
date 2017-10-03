# -*- coding: utf-8 -*-
import math

#COMECE SEU CODIGO AQUI

n = int(input( 'Digite o valor desejado'))

while(n>=20):
    n = n-20
    nota20=nota20+1
    
while(n>=10):
    n = n-10
    nota10=nota10+1

while(n>=5):
    n = n-5
    nota5=nota5+1

while(n>=2):
    n = n-2
    nota2=nota2+1
    
while(n>=1):
    n = n-1
    nota1=nota1+1
    
print(nota20)
print(nota10)
print(nota5)
print(nota2)
print(nota1)

    
    
    