# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
n = int(input( 'informe a quantidade de notas: '))
notas = []
if n> 1:
    for i in range(0,n,1):
        notas.append(float(input('digite a nota%d: ' % ( i+1))))
    media = 0
    for i in range(0,n,1):
        media += notas[i]/n
    print(notas)
    print(media)
else:
    print('informe n maior q 1')




