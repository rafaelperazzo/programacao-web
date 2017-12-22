# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
n = int(input('Digite a quantidade de notas :'))
notas = []
for i in range(0,n,1):
    notas.append(float(input('Digite a nota%d: ' % (i+1))))
dmh = 0
 for i in range(0,n,1):
    dmh += 1.0/notas[i]
mh = n / mdh    
    print(mh)