# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('digite o numero de pessoas:'))
m=masculino
f=feminino
maior=0
menor=3.00
cont=0
for i in range(1,n+1,1):
    x=float(input('digite a altura:'))
    a=input('digite o sexo:')
    
    if x>maior:
        maior=x
    if x<menor:
        menor=x
    if a==m:
        cont=cont+1
    if a==f:
        cont=cont        
porcentagem=(cont/n)*100    
    
print(maior)
print(menor)
print(porcentagem)