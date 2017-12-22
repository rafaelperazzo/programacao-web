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

notas=[]
for i in range(0,5,1):
    notas.append(float(input('Digite o elemento: ')))
media=0
for i in range(0,5,1):
    media += notas[i]/5.0
    print(media)
print(notas)

n= int(input('Digite uma quantidade de notas: '))
notas= []

for i in range (0,n,1):
    notas.append(float(input('Digite a nota%d: ' % (i+1))))

denominador_harmonico = 0

for i in range(0,n,1):
   denominador_harmonico += 1.0/notas[i]
media_harmonica = n / denominador_harmonico
print(media_harmonica)
'''
n=4
a=[]
for i in range(0,n,1):
    a.append(int(input('Digite um valor: ')))
soma=0

for i in range(0,n,1):
    soma = (a[i]**2)
    
print(soma)










