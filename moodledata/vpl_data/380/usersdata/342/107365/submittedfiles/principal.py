import random
nome = input('Insira o nome do usuário:')

def solicitaSimboloDoHumano():
    simb = ''
    while simb != 'X' or 'O':
        print ('Escolha um simbolo desejado')
        simb  = input('Escolha o seu símbolo:')
        
    
solicitaSimboloDoHumano()
        

print(random.choice([nome,'computador começa']))

