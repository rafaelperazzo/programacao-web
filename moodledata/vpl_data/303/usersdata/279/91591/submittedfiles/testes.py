# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

notas=[]
for i in range (0,51,1) :
   notas.append(float(input('digite a nota%d:' % (i+1))))
media = 0
for i in range (0,51,1) :
   media += notas[i]/5.0
print(notas)
print(media)






