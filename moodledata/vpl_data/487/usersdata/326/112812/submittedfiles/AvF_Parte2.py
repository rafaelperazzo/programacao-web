# -*- coding: utf-8 -*-
usuario = input('Digite seu nome de usuario: ')
senha = input('Digite sua senha: ')
while usuario == senha:
    input('Digite uma senha diferente do nome de usuario: ')
    break
print('ENTROU')