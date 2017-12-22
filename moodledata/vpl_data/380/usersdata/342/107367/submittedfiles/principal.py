import random
nome = input('Insira o nome do usuário:')

def solicitaSimboloDoHumano():
    simb = input('Escolha o seu símbolo:')
    while simb != 1 or 2 :
        simb  = input('Escolha um simbolo válido')
        
    
solicitaSimboloDoHumano()
        

print(random.choice([nome,'computador começa']))

