import random
nome = input('Insira o nome do usuário:')

def solicitaSimboloDoHumano():
    simb = input('Escolha o seu símbolo:')
    while (simb != 'X'):
        simb  = input('Escolha um simbolo válido')
        
    
solicitaSimboloDoHumano()
        

print(random.choice([nome,'computador começa']))

