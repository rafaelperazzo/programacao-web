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
n = str(input('insira o seu nome: '))
while (True):
    se = (input('escolha uma senha:'))
    if (str(n) == str(se)):
        s = str(input('insira uma senha:'))
        se = s
    else:
        break
    
print ('ENTROU')