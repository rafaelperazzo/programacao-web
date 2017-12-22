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
'''#deviopadrao
n=int(input('digite o numero de elementos da lista: '))
lista=[]
somatorio=0
for i in range(0,n,1):
    lista.append(float(input('insira um valor a lista: ')))
media=sum(lista)/float(n)
for i in range(0,n,1):
    somatorio = somatorio + ((lista[i]-media)**2)
desvpad=((1/(n-1))*somatorio)**(0.5)
print(desvpad)'''
import numpy as np
matriz=[]
m=int(input('digite o numero de linhas da matriz que voceh deseja recortar: '))
n=int(input('digite o numero de colunas da matriz que voceh deseja recortar: '))
for i in range(0,m,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(int(input('digite o valor do elemento da linha%d e da coluna%d desejada: '%((i+1),(j+1)))))
        matriz.append(linha)
linhaszeradas=0
linhaszeradas2=0
colunaszeradas=0
colunaszeradas2=0
#corte superior
for i in range(0,m-1,1) :
     y=sum(matriz[i])
    if y > 0 :
        break
    else :
        linhaszeradas=linhaszeradas+1
    if linhaszeradas>0 :
        for i in range(0,linhaszeradas,1):
            del matriz[i]
#corte inferior
for i in range(m-linhaszeradas-1,0,-1) :
    r=int(sum(matriz[i]))
    if r > 0 :
        break
    else :
        linhaszeradas2=linhaszeradas2+1
if linhaszeradas2>0:
    for i in range(m-1,m-linhaszeradas2-1,-1):
       del matriz[i]
t=0
#corte direito
for i in range(0,m-linhaszeradas-linhaszeradas2,1):
    for j in range(0,n,1) :
        if i+1<m-linhaszeradas-linhaszeradas2 :
            t=t+matriz[i][j]+matriz[i+1][j]
            if t > 0 :
                break
            else :
                colunaszeradas=colunaszeradas+1
if colunaszeradas > 0:
    for i in range(0,m-linhaszeradas-linhaszeradas2,1):
        for j in range(colunaszeradas-1,0,-1):
            del matriz[i][j]
#corte esquerdo
f=0
for i in range(0,m-linhaszeradas-linhaszeradas2,1):
    for j in range(n-colunaszeradas-1,0,-1) :
        f=f+matriz[i][j]
        if f > 0 :
            break
        else :
            colunaszeradas2=colunaszeradas2+1
if colunaszeradas2>0 :
    for i in range(0,m-linhaszeradas-linhaszeradas2,1):
        for j in range(n-colunaszeradas-colunaszeradas2,n-colunaszeradas-colunaszeradas2-1,-1):
            del matriz[i][j]
#saida
print(matriz)