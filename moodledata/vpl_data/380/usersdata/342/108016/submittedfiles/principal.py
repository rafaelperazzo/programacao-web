import random
nome = input('Insira o nome do usuário:')

'''       
def sorteioPrimeiraJogada():
    print(random.choice([nome,'Computador começa']))
 
sorteioPrimeiraJogada()
'''

tab = []
for i in range (3):
    v = []
    for j in range(3):
        v.append('  ')
    tabuleiro.append(v)
    
n = input('jogada   ')
i = int(n[0])
j = int(n[1])
tabuleiro [i][j] = 'x'
print (tabuleiro)