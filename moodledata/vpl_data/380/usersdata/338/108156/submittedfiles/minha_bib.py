
"""
nome_do_jogador = input("Digite o seu nome: ")
simb = input("Digite o simbolo com o qual vocÊ quer jogar [X ou O] : ")

while(True):
    if simb == "X" or simb == "O" :
        break
    else:
        simb = input("Digite um simbolo válido %s : " % nome_do_jogador) 


j_d_v1 = [" ", " ", " "]
j_d_v2 = [" ", " ", " "]
j_d_v3 = [" ", " ", " "]     

cordenadas1 = ["00", "01", "02"]
cordenadas2 = ["10", "11", "12"] 
cordenadas3 = ["20", "21", "22"] 

print(" ")
print(" ")
print(' ' + cordenadas1[0] + ' | ' + cordenadas1[1] + ' | ' + cordenadas1[2])
print('----+----+----')
print(' ' + cordenadas2[0] + ' | ' + cordenadas2[1] + ' | ' + cordenadas2[2]) 
print('----+----+----')
print(' ' + cordenadas3[0] + ' | ' + cordenadas3[1] + ' | ' + cordenadas3[2])   

print(" ")
print(" ")
print(' ' + j_d_v1[0] + ' | ' + j_d_v1[1] + ' | ' + j_d_v1[2]) 
print('---+---+---')
print(' ' + j_d_v2[0] + ' | ' + j_d_v2[1] + ' | ' + j_d_v2[2])
print('---+---+---')
print(' ' + j_d_v3[0] + ' | ' + j_d_v3[1] + ' | ' + j_d_v3[2])
print(" ")
print(" ")


from time import sleep


print("")
print("========================================================================")    
print("")
print("Okay %s Seu simbolo foi aceito" % nome_do_jogador )
sleep(1.5)
print("O seu simbolo será o: %s" % simb)
sleep(1.5)
print("BOA SORTE!!!")
print("")
print("========================================================================") 

sleep(1)
print("")
print("Agora sortearemos quem irá começar o jogo")
sleep(2)

import random
a = random.randint(1,2)
if a==1:
    print("Você começa %s" % nome_do_jogador )
    print("Escolha uma coordenada")
   
    print(" ")
    print(" ")
    print(' ' + cordenadas1[0] + ' | ' + cordenadas1[1] + ' | ' + cordenadas1[2])
    print(' ' + cordenadas2[0] + ' | ' + cordenadas2[1] + ' | ' + cordenadas2[2])
    print(' ' + cordenadas3[0] + ' | ' + cordenadas3[1] + ' | ' + cordenadas3[2])

elif a==2 :
    print("O computador começou jogando agora é sua vez %s" % nome_do_jogador)
    print(" ")
    print(" ")
    print(' ' + cordenadas1[0] + ' | ' + cordenadas1[1] + ' | ' + cordenadas1[2])
    print(' ' + cordenadas2[0] + ' | ' + cordenadas2[1] + ' | ' + cordenadas2[2])
    print(' ' + cordenadas3[0] + ' | ' + cordenadas3[1] + ' | ' + cordenadas3[2])

j_d_v1 = [" ", " ", " "]
j_d_v2 = [" ", " ", " "]
j_d_v3 = [" ", " ", " "] 

n = input("Digite a jogada: ")
i = n[0]
j = n[1]

print(i,j)
"""
#n = input('Digite sua jogada: ')

if n[0] == 0:
    tabuleiro1[n[1]] = simb
    print(" ")
    print(tabuleiro1[0] + '  ' + "|" + tabuleiro1[1] + ' ' + "|" + tabuleiro1[2]) 
    print('---+--+---')
    print(tabuleiro2[0] + '  ' + "|" + tabuleiro2[1] + ' ' + "|" + tabuleiro2[2])
    print('---+--+---')
    print(tabuleiro3[0] + '  ' + "|" + tabuleiro3[1] + ' ' + "|" + tabuleiro3[2]

if n[0] == 1:
    tabuleiro2[n[1]] = simb
    

if n[0] == 2:
    tabuleiro3[n[1]] = simb

#jogo_d_v[int(n[0])] [int(n[1])] = "X"

#print(jogo_d_v[0][0] + "|" + jogo_d_v[0][1] + "|" + jogo_d_v[0][1]) 
#print(jogo_d_v[1][0] + "|" + jogo_d_v[1][1] + "|" + jogo_d_v[1][2])
#print(jogo_d_v[2][0] + "|" + jogo_d_v[2][1] + "|" + jogo_d_v[2][2])
