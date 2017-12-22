# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

while True:
    a=int(input('digite o valor de n: '))
    if a>0:
      break
soma=0

while a<=1:
    i=a//10
    r=a%10
    soma=soma+r
    a=a//10
    
print(soma)
    
