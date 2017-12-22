# -*- coding: utf-8 -*-
nome= input('Nome de usuário: ')
senha= input('Senha: ')

while senha==nome:
    senha= input('Senha: ')
    if senha != nome:
        break
print('ENTROU')