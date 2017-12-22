import random
nome = input('Insira o nome do usuário:')

def solicitaSimboloDoHumano():
    simb = input('Escolha o seu símbolo:')
    while simb != 'X' or 'O':
        print ('Escolha um símbolo válido')
        if simb == 'X' or 'O':
            continue
    
solicitaSimboloDoHumano()
        



