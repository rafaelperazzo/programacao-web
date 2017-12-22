# -*- coding: utf-8 -*-
N = int(input('Digite a quantidade de alunos: '))
P = int(input('Digite a quantidade minima de pontos: '))



for i in range (0,N,1):
    primeiranota = float (input('Digite a primeira nota: '))
    segundanota = float (input('Digite a segunda nota: '))
    pontos = primeiranota + segundanota
    if pontos > P:
        cont = cont + 1
    pontos = 0
    
print (cont)
