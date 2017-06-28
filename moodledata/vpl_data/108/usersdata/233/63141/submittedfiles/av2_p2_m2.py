# -*- coding: utf-8 -*-
n=int(input('Digite o número de salas: '))
salas=[]
for i in range(n):
    vidaporsala=int(input('Vida desta sala: '))
    salas.append(vidasporsala)
entrada=int(input('Sala de entrada: '))
saída=int(input('Sala de saída: '))
soma=0
for i in range(entrada,saída+1,1):
    soma=soma+salas[i]
print('%.d'%soma)
