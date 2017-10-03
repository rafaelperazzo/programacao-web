# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
a = int(input('Que horas são? [0-23] '))
if a > 3 and a < 12:
    print('Bom dia')
elif a >= 12 and a < 18:
    print('Boa Tarde')
elif a >= 18 and a < 3:
    print('Boa Noite')
else:
    print('n exisy')