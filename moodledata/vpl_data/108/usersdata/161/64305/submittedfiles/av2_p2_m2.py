# -*- coding: utf-8 -*-
n=int(input('Informe a quantidade de salas:'))
lista=[]
for i in range(1,n+1,1):
    v=int(input('Informe a quantidade de vidas:'))
    lista.append(v)
 
a=int(input('Informe o número da sala de entrada:'))
b=int(input('Informe o número da sala de saída:'))
   
vidas=0
for i in range(a,b+1,1):
        vidas=vidas+lista[i]
print(vidas)    
    

