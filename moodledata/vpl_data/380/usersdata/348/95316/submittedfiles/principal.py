# -*- coding: utf-8 -*-

#COMECE AQUI ABAIX

n = int(input( 'informe n'))

a = []
for i in range (0,n,1):
    a.append(int(input('digite o valor: ')))
for i in range(0,n,1):
    if a[i]%2 == 0:
        print(a[i])





'''
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




