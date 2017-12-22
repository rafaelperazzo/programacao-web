# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
'''
n= int(input('Digite uma quantidade de notas: '))

if n>1:
    print(n)
else:
    print(int(input('Quantidade inválida, digite novamente: ')))
    
notas=[]

for i in range (0,n,1):
    notas.append(float(input('Digite a nota%d: ' % (i+1))))
    
media=0
for i in range(0,n,1):
    media += notas[i]/float(n)
print(notas)
print(media)
'''
notas=[]
for i in range(0,6,1):
    notas.append(input('Digite o elemento: '))
    print(notas)

