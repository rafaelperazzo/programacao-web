# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
idade = int(input('Digite sua idade: '))
print('Sua idade é',idade,'!')
if int(idade) < 18:
    print('Você tem menos de 18 anos :(!')
elif int(idade) == 18:
    print('Você tem 18 anos :)!')
else:
    print('Você tem mais de 18 anos :D!')
