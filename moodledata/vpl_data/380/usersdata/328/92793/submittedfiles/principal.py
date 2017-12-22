# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
notas=[]
#media=(notas[0] + notas [1] + notas [2])
print ('%.2f'%media)
for i in range(0,5,1):
    notas.append(float(input('Digite a nota%d: ' % (i+1)))
media=0
for i in range(0,5,1):
    media+=notas[i]/5
print (notas)
print (media)