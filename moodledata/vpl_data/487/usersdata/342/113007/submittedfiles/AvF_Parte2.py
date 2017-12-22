# -*- coding: utf-8 -*-
'''
n = str(input('insira o seu nome: '))
se = (input('escolha uma senha:'))

while (True):
    if (str(n) == str(se)):
        print ('insira uma senha válida')
        
    else:
        break
print ('ENTROU')
'''

while (True):
    n = str(input('insira o seu nome: '))
    se = (input('escolha uma senha:'))
    if (str(n) == str(se)):
        s = str(input('insira uma senha válida:'))
        se = s
    else:
        break
    
