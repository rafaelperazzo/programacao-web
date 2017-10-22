# -*- coding: utf-8 -*-
a=int(input('Digite o valor da moeda 1: '))
b=int(input('Digite o valor da moeda 2: '))
c=int(input('Digite o valor da cédula: '))

cont=0
while(c>=a):
    conta=conta+1
    c=c-a
    while(c>=b):
        contb=contb+1
        c=c-b
        
print(conta)
print(contb)

while(c>=b):
    contb=contb+1
    c=c-b
    while(c>=a):
        conta=conta+1
        c=c-a
        
print(conta)
print(contb)
    
    
    
        