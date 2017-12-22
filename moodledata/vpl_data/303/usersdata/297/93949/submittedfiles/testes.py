# -*- coding: utf-8 -*-
'''n=int(input('digite um n,inteiro e positivo: '))
i=1
fat=1
while (n<0) :
    n=int(input('opcao invalida,digite um inteiro positivo; '))
while i<=n :
    fat= i*fat
    i=i+1
print("%d"%fat)'''
'''notas=[]
for i in range (0,5,1):
    notas.append(float(input('digite a nota%d: '%(i+1))))
media=0
for i in range (0,5,1):
    media+=notas[i]/5.0
print(notas)
print(media)'''
'''n=int(input('digite o numero de notas desejado: '))
while n<=1 :
    n=int(input('digite o numero de notas desejado: '))
notas=[]
for i in range (0,n,1):
    notas.append(float(input('digite a nota%d: '%(i+1))))
media=0
for i in range (0,n,1):
    media+=notas[i]/n
print(notas)
print(media)'''
#deviopadrao
n=int(input('digite o numero de elementos da lista: '))
lista=[]
somatorio=0
for i in range(0,n,1):
    lista.append(float(input('insira um valor a lista: ')))
media=sum(lista)/float(n)
print(media)
for i in range(0,n,1):
    somatorio = somatorio + ((lista[i]-media)**2)
print(somatorio)
desvpad=((1/n-1)*somatorio)**0.5
print(desvpad)
