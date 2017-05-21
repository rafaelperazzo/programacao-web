# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
leitura=int(input('Digite'))
senha=222
if leitura==senha:
        print('Congratulations')
while leitura!=senha:
    print('Password is wrong. Try again')
    leitura=int(input('Digite'))
    if leitura==senha:
        print('Congratulations')
        