# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
'''
import time
n=int(input('Numero de notas: '))
while n<1:
    n=int(input('Numero de notas: '))
notas=[]  
for i in range(0,n,1):
    notas.append(float(input('Digite a nota %d: ' %(i+1))))
dh = 0
for i in range(0,n,1):
    dh += 1/notas[i]
    print('fraçao: 1/' +str(notas[i]))
    print('dh apos soma: ' + str(dh))
    time.sleep(3)
mh=n/dh    
print(mh)
#print(media)
'''
import math

n=int(input('quant de elemenos: '))
a=[]
for i in range (0,n,1):
    a.append(input('valor: '))
    soma=a[i]
    for i in range(1,n+1,1):
        soma = soma + (a[i]**2)
print(soma)
    

