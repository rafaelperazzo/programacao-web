# -*- coding: utf-8 -*-
n = str(input('insira o seu nome: '))
se = (input('escolha uma senha:'))

while (True):
    if (str(n) == str(se)):
        print ('indira uma senha válida')
        if (str(n) != str(se)):
            break
    else:
        break
print ('ENTROU')
