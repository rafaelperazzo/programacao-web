import random
nome = input('Insira o nome do usuário:')

def solicitaSimboloDoHumano():
    simb = input('Escolha o seu símbolo:')
    while (simb != ('X'or 'O')):
        simb  = input('Escolha um simbolo válido')
        
solicitaSimboloDoHumano()
        
def sorteioPrimeiraJogada():
    print(random.choice([nome 'começa','computador começa']))


