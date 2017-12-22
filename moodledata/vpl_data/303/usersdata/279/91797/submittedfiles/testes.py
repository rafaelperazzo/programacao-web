# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
'''n=int(input("Digite a quantidade de notas"))
notas=[]
for i in range (0,n,1) :
   notas.append(float(input('digite a nota%d:' % (i+1))))
media = 0
for i in range (0,n,1) :
   media += notas[i]/n
print(notas)
print(media)'''

a = []
for i in range (1,4,1) :
    a.append(float(input('Digite o elemento : ')))
print(a)
print(sum(a))
print(len(a))
print(8 in a)
del a[1]
print(a)
print(len(a))

