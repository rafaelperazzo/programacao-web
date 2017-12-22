# -*- coding: utf-8 -*-
x= int(input('Digite a quantidade de portas:'))
b= []

for i in range (0,x,1):
    vidasporsala= int(input('Digite a quantidade de vidas por sala:'))
    b.append (vidasporsala)
    
entrada= int(input('Digite a porta de entrada:'))
saida= int(input('Digite a porta de saida:'))

soma=0

for i in range (entrada,saida+1,1):
    soma= soma+b[i]
    
print (soma)