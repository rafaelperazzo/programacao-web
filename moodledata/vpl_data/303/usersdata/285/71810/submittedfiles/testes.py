# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
# Entrada
a = int(input('Que horas são? [0-23] '))
# Processamento e saída
if a < 0 or a > 23:
    print('Hora invalida')
else:
    if a > 3 and a < 12:
    print('Bom dia')
elif a >= 12 and a < 18:
    print('Boa tarde')
elif:
    print('Boa noite')
 