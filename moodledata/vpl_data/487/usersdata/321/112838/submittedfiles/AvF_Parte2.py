# -*- coding: utf-8 -*-
nome= input('Nome de usuário: ')
senha= input('Senha: ')

while nome==senha:
    senha= input('Senha: ')
    if senha != nome:
        break
print('ENTROU')