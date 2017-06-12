# -*- coding: utf-8 -*-
a1=int(input('1° numero da aposta:'))
a2=int(input('2° numero da aposta:'))
a3=int(input('3° numero da aposta:'))
a4=int(input('4° numero da aposta:'))
a5=int(input('5° numero da aposta:'))
a6=int(input('6° numero da aposta:'))
b1=int(input('1° numero sorteado:'))
b2=int(input('2° numero sorteado:'))
b3=int(input('3° numero sorteado:'))
b4=int(input('4° numero sorteado:'))
b5=int(input('5° numero sorteado:'))
b6=int(input('6° numero sorteado:'))
lista1=[a1,a2,a3,a4,a5,a6]
lista2=[b1,b2,b3,b4,b5,b6]
cont=0
for i in range (0,len(lista1),1):
for j in range (0,len(lista2),1):
if lista1[i]-lista2[j]==3:
    print('terno')
        
    
 