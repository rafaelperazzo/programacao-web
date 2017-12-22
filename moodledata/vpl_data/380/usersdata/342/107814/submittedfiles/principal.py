import random
nome = input('Insira o nome do usuário:')

def solicitaSimboloDoHumano():
    simb = input('Escolha o seu símbolo:')
    while(True): 
        if simb == 'x' or simb == 'o':
            break
        else:
            simb  = input('Escolha um simbolo válido')
        
solicitaSimboloDoHumano()
        
def sorteioPrimeiraJogada():
    print(random.choice([nome,'Computador começa']))
    
sorteioPrimeiraJogada()


solicitaSimboloDoHumano()
solicitaSimboloDoHumano()
solicitaSimboloDoHumano()


