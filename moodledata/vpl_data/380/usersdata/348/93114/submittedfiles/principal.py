# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO

n = int(input( 'informe a quantidade de notas: '))
notas = []

while n <= 1:
    n = int(input( 'informe a quantidade de notas: '))

for i in range(0,n,1):
    notas.append(float(input('digite a nota%d: ' % ( i+1))))

media = sum(notas)/float(len(notas))
print(notas)
print(media)





