import random
nome = input('Insira o nome do usuário:')

def solicitaSimboloDoHumano():
    simb = input('Escolha o seu símbolo:')
    if simb == 'X' or 'O':
        break
    else:
        print ('escolha um símbolo válido')
        
    
solicitaSimboloDoHumano()
        

print(random.choice([nome,'computador começa']))

