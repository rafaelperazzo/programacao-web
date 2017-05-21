# -*- coding: utf-8 -*-
n = int(input('Digite um numero qualquer: '))
cont = 0

while n>0:
    n = n//10
    cont=cont+1

print (cont)    
