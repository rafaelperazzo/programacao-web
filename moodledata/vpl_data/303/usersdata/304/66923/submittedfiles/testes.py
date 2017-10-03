# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
idade = int(input('Digite sua idade: '))
print('A idade do indivíduo é',idade,'!')
if int(idade) < 18:
    print('Você tem menos de 18 anos :(!')
elif int(idade) == 18:
    print('Você tem 18 anos :)!')
else:
    print('Você tem mais de 18 anos :D!')
altura = float(input('Digite sua altura: '))
if float(altura) <= 1.50:
    print('Você é um smurf!')
elif float(altura) >1.50 < 1.70:
    print('Você é normal')
else:
    print('Você é um avatar!')
print('Razão idade/altura = ',idade/altura)
    