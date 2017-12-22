# -*- coding: utf-8 -*-
n= int(input('Digite o número de participantes:'))
p= int(inut('Digite a pontuação mínima:'))
cont=0

for i in range (0,n,1):
    x= int(input('Digite a primeira pontuação:'))
    y= int(input('Digite a segunda pontuação:'))
    if (x+y)>=p:
        cont= cont+1
        
print (cont)
