# -*- coding: utf-8 -*-
from os import system as sy
from time import sleep as slp
while True:
    x = input('Informe o valor em binário: ')
    expoente = 0
    total = 0
    for numero in range(len(x)-1, -1, -1):
        total += int(numero)**expoente
        expoente += 1
    print(total)
    slp(2)
    sy('clear')



'''
#COMECE AQUI ABAIX

n = int(input( 'informe n'))

a = []
for i in range (0,n,1):
    a.append(int(input('digite o valor: ')))
print(a[len(a)-1])







n = int(input( 'informe a quantidade de notas: '))

while n <= 1:
    n = int(input( 'informe a quantidade de notas: '))
notas = []

for i in range(0,n,1):
    notas.append(float(input('digite a nota%d: ' % ( i+1))))
denominador = 0

for i in range (0,n,1):
    denominador += 1.0/notas[i]
print(denominador)
'''




