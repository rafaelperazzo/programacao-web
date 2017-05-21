# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
leitura=int(input('Digite'))
senha=222
while leitura!=senha:
    leitura=int(input('Digite'))
    if leitura==senha:
        print('Congratulations')
    else:
        print('ERROR')
        