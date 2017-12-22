#from minha_bib import *
# -*- coding: utf-8 -*-

notas = []
for i in range(0,5,1):
    notas.append(float(input('Digite a nota%d: ' % (i+1))))
media = sum(notas)/len(notas)
#for i in range(0,5,1):
#    media += notas[i]/5.0
print(notas)
print(media)
if 2 in notas:
    print(notas.index(2))
else:
    print('2 nao ta na lista de notas')

del lista[2]