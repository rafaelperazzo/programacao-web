# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
a = int(input('Que horas são? '))
if a > 3 and a < 12:
    print('Bom dia')
elif a >= 12 and a < 18:
    print('Boa tarde')
elif a >= 18 and a <= 23:
    print('Boa noite')
elif a > 0 and a < 3:
    print('Boa noite')
else:
    print('Tá maluco parça')