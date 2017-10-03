# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
nome= str(input('Qual o seu nome? '))
print('Olá ' +nome+ ' seja bem vinda!')
idade= int(input('Qual a sua idade? '))
altura= float(input('Qual a sua altura? '))
print('Você tem %d anos e %.2f metros de altura' %(idade, altura))
if altura<1.60 and idade>15:
    print('Nossa, você é uma nanica!\n')
    print('Desculpe pela sinceridade')
else:
    print('Girafa')