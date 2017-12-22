# -*- coding: utf-8 -*-
usuario = input('Digite seu nome de usuario: ')
senha = input('Digite sua senha: ')
while usuario == senha:
    senha = input('Digite sua senha: ')
    if senha != usuario:
        print('ENTROU')