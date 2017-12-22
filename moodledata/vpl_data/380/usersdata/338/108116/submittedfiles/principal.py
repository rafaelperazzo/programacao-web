import random
from time import sleep
#######################################################################################

def solicita_simbolo(simb):
    while(True):   #Verifica se o simbolo é vàlido
        if simbj == "X" or simbj == "O" :
            break
        else:
            simbj = input("Digite um simbolo válido %s : " % nome_do_jogador)
        

def sorteio_primeira_jogada():
    print(random.choice(['Você começará','computador ganhou ele começa']))
    
def recebe_e_validar_jogada():
    n = input('Digite sua jogada: ')
    while(True): 
        if int(n[0]) >= 0 and int(n[0]) < 3 :
            if int(n[1]) >= 0 and int(n[1]) < 3:
                break
        else:
            n = input('Digite uma jogada válida %s: ' % nome_do_jogador)
    i = int(n[0])
    j = int(n[1])

    tabuleiro[i][j] = simbj
    
""" 
def jogada_do_computador():
    n = random.choice([00,01,02,10,11,12,22,20,21])
    while(True): 
        if :
            if int(n[1]) >= 0 and int(n[1]) < 3:
                break
        else:
            n = input('Digite uma jogada válida %s: ' % nome_do_jogador)
    i = int(n[0])
    j = int(n[1])

    tabuleiro[i][j] = simbc
"""    

#######################################################################################


nome_do_jogador = input("Digite o seu nome: ") #Pede o nome do jogador

simbj = input("Digite o simbolo com o qual vocÊ quer jogar [X ou O] : ")
solicita_simbolo(simbj)

print('Agora sortearemos quem começará: ')
sleep(1.5)
sorteio_primeira_jogada()


#-----------------------------------------------------##-----------------------------------------------------##-----------------------------------------------------#

coordenadas = [
            ('00', '01', '02')
            ,('10', '11','12')  #Matriz das coordenadas
            ,('20','21','22')
            ]

tabuleiro = [
            (' ', ' ', ' ')
            ,(' ', ' ', ' ')  #matriz tabuleiro
            ,(' ', ' ', ' ')
            ]
            
print(" ")
print(coordenadas[0][0]  + "|" + coordenadas[0][1] + ' ' + "|" + coordenadas[0][2]) 
print('---+--+---')
print(coordenadas[1][0]  + "|" + coordenadas[1][1] + ' ' + "|" + coordenadas[1][2])    #print coordenadas
print('---+--+---')
print(coordenadas[2][0]  + "|" + coordenadas[2][1] + ' ' + "|" + coordenadas[2][2])
sleep(1)
print(" ")
print(tabuleiro[0][0] + '  ' + "|" + tabuleiro[0][1] + ' ' + "|" + tabuleiro[0][2]) 
print('---+--+---')
print(tabuleiro[1][0] + '  ' + "|" + tabuleiro[1][1] + ' ' + "|" + tabuleiro[1][2])    #print tabuleiro
print('---+--+---')
print(tabuleiro[2][0] + '  ' + "|" + tabuleiro[2][1] + ' ' + "|" + tabuleiro[2][2])


tabuleiro = []
for i in range (3):
    v = []
    for j in range(3):
        v.append(' ')
    tabuleiro.append(v)
    
recebe_valida_jogada()
        



print(" ")
print(coordenadas[0][0]  + "|" + coordenadas[0][1] + ' ' + "|" + coordenadas[0][2]) 
print('---+--+---')
print(coordenadas[1][0]  + "|" + coordenadas[1][1] + ' ' + "|" + coordenadas[1][2])
print('---+--+---')
print(coordenadas[2][0]  + "|" + coordenadas[2][1] + ' ' + "|" + coordenadas[2][2])
sleep(0.7)
print(" ")
print(tabuleiro[0][0] + '  ' + "|" + tabuleiro[0][1] + ' ' + "|" + tabuleiro[0][2]) 
print('---+--+---')
print(tabuleiro[1][0] + '  ' + "|" + tabuleiro[1][1] + ' ' + "|" + tabuleiro[1][2])
print('---+--+---')
print(tabuleiro[2][0] + '  ' + "|" + tabuleiro[2][1] + ' ' + "|" + tabuleiro[2][2])
print(' ')


        
        
        
        
        
        
        
        
        