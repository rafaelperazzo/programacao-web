import random
nome = input('Insira o nome do usuário:')
X = 1
O = 2
def solicitaSimboloDoHumano():
    simb = input('Escolha o seu símbolo:')
    while (simb != 1 or 2):
        simb  = input('Escolha um simbolo válido')
        
solicitaSimboloDoHumano()
        
def sorteioPrimeiraJogada():
    print(random.choice([nome,'Computador começa']))
    
sorteioPrimeiraJogada()


