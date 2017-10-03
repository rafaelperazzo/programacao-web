# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
nota1 = float(input('insira a nota 01:'))
nota2 = float(input('insira a nota 02:'))

m=(nota1+nota2)/2
print ('media= %.2f' %m)
if m>=6 :
    print ('aprovado')
elif m>=4:
    print ('avf')
else :
    print ('reprovado')