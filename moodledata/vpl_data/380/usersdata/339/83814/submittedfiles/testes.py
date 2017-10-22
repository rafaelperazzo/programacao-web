# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO




leitura = input('Digite sua Senha: ')
Senha = '12345'


while (leitura != Senha):
    leitura = input('Digite sua Senha: ')
    if leitura==Senha:
        print('acertou mizera')
    else:
        print('erow')