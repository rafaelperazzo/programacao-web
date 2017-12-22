
'''s = str(input('Informe seu sexo :')).strip().upper()[0]
while s not in 'MmFf':
    s = str(input("Dados invalido. Digite novamente ")).strip().upper()[0] 
print(s)'''

from random import randint
computador = randint(0,10)
print('Acabei de jogar um numero entre 0 e 10.')
print('Sera que voce adivinha ?')
acertou = False
while not acertou:
    jogador = int(input('Qual o seu palpite :'))
    if jogador == computador:
        acertou = True 