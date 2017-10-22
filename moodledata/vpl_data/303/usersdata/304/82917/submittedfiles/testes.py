# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
'''
-------------------------------------------------

p1 = float(input('Insira o peso 1: '))
c1 = float(input('Insira o comprimento 1: '))
p2 = float(input('Insira o peso 2: '))
c2 = float(input('Insira o comprimento 2: '))
if (p1*c1) == (p2*c2):
    print('0')
elif (p1*c1) > (p2*c2):
    print('-1')
else:
    print('1')

-------------------------------------------------
'''
'''
#-------------------------------------------------
#MOSTRA TODOS OS NÚMEROS PARES [0,100]
i = 0
while (i<=100):
    if i%2 == 0:
        print(i)
    i += 1
    
#-------------------------------------------------
'''
'''
#-------------------------------------------------
#SOMA TODOS OS NÚMEROS ÍMPARES [O,n[
n = int(input('n: '))
i = 1
cont = 0
while i < n:
    if i%2==1:
        cont = cont + 1
    i = i + 1
print (cont)

#-------------------------------------------------
'''
'''
#-------------------------------------------------
#LOOP INFINITO DE 0
i = 0
while (i<10):
    print(i)
    
#-------------------------------------------------
'''
#'''
#-------------------------------------------------
#MOSTRA O QUADRADO DOS NÚMEROS ÍMPARES [0,n]
i = 1
n = int(input('n: '))
while n <= 0:
    n = int(input('n: '))
while i <= n:
    print (i**2)
    i=i+2
    
#-------------------------------------------------
#'''
'''
-------------------------------------------------

n = int(input('n: '))
i = 1
cont = 0
while i < n:
    if i%2==1:
        cont = cont + i
    i = i + 1
print (cont)

-------------------------------------------------
'''
'''
n = int(input('Digite um nº com 8 algarismos: '))
while n<9999999 and n>99999999:
    n = int(input('Digite um nº com 8 algarismos: ')
    '''