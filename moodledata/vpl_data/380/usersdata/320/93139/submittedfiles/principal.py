# -*- coding: utf-8 -*-
n = int(input('Digite o numero de notas: '))
notas = []
for i in range (0, n, 1):
    notas.append(float(input('Digite a nota%d: ' % (i+1))))
media = sum(notas)/float(len(notas))
for i in range (n, -1, -1):
    print (notas[i])
print (media)
