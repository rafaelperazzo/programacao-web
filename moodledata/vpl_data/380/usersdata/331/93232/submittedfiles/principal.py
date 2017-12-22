# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
n = int(input('digite o numero de notas:'))
while n<=1:
    n = int(input('digite o numero de notas:'))
notas = []
for i in range (0,n,1):
    notas.append(float(input('digite a nota %d:' % (i+1))))
media = float(sum(notas)/len(notas))
for i in range (0,n,1):
    print (notas[i])
print (media)