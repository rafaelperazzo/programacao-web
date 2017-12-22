# -*- coding: utf-8 -*-
import numpy as np
import funcoes

#ENTRADA
dimensao = input('Digite a dimensao das matrizes: ')
matrizA = input('Digite a Matriz A como uma única linha entre aspas: ')
matrizD = input('Digite a Matriz D como uma única linha entre aspas: ')
alfa = input('Digite o valor de alfa: ')

#PREPARANDO A ENTRADA
T = np.zeros((dimensao,dimensao))
A = np.fromstring(matrizA, sep=' ').reshape(dimensao, dimensao)
d = np.fromstring(matrizD, sep=' ').reshape(dimensao, dimensao)

#comece aqui...
#INÍCIO
a = funcoes.somacoluna(A)
o = funcoes.somalinha(A)
#SOMATÓRIOCOLUNA
#ELEMENTOT
numerador = a[j]/(d[i,j]**alfa)
somatorio1 = 0
for k in range (0,dimensao,1) :
    somatorio1 = somatorio1 + (a[k]/d[i,k])
denominador = somatorio1
for i in range (0,a.shaped[0],1) :
    for j in range (0,a.shaped[1],1) :
        T[i,j] = o[i] * (numerador/denominador)
#SAIDA


            

            
    




#SAÍDA

somatorio = sum(sum(T))
print('%.4f' % somatorio)
