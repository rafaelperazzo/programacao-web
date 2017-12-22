# -*- coding: utf-8 -*-
n=int(input('Digite o número de termos: '))
lista=[]

for i in range (0,n,1):
    lista.append(int(input('Digite o valor da lista: ')))
    
cont=0
if lista[1]>lista[0] and lista[1]>lista[2]:
    cont=cont+1
    
cont1=0
if lista[n-2]>lista[n-1] and lista[n-2]>lista[n-3]:
    cont1=cont1+1
    
cont2=0
for i in range(1,n-1,1):
    if lista[i]>lista[i+1] and lista[i]>lista[i-1]:
        cont2=cont2+1

lista2=[]


for i in range(0,n,1):
    lista2.append(int(input('Digite o valor da lista2: ')))
    
cont3=0
if lista2[1]>lista2[0] and lista2[1]>lista2[2]:
    cont3=cont3+1
cont4=0
if lista2[n-2]>lista[n-1] and lista2[n-2]>lista[n-3]:
    cont4=cont4+1
    
cont5=0
for i in range(1,n-1,1):
    if lista2[i]>lista2[i+1] and lista2[i]>lista2[i-1]:
        cont5=cont5+1
        
if cont==0 or cont1 == 0 or cont2 == 0:
    print('S')
else:
    print('N')
if cont==3 or cont1==4 or cont2==5:
    print('S')
else:
    print('N')
    
    
    
    
    
    
    