# -*- coding: utf-8 -*-
n=int(input('Digite o número de salas: '))
salas=[]
for i in range(n):
    vidaporsala=int(input('Vida desta sala: '))
    salas.append(vidaporsala)
entrada=int(input('Sala de entrada: '))
saída=int(input('Sala de saída: '))
soma=0
if saída>entrada:
    for i in range(entrada,saída+1,1):
        soma=soma+salas[i]
elif entrada>saída:
    for i in range(saída,entrada-1,-1):
        soma=soma+salas[i]    
print('%.d'%soma)
