import random
nome = input('Insira o nome do usuário:')

'''       
def sorteioPrimeiraJogada():
    print(random.choice([nome,'Computador começa']))
 
sorteioPrimeiraJogada()
'''
def validaJogada(n):
    while (true):
        if (2>=(n[o] and n[1])>=0):
            break
        else:
            print('digite uma casa válida')
        

tabuleiro = []
for i in range (3):
    v = []
    for j in range(3):
        v.append('  ')
    tabuleiro.append(v)
    
n = input('jogada   ')
validaJogada(n)
i = int(n[0])
j = int(n[1])
tabuleiro [i][j] = 'x'
print (tabuleiro)




