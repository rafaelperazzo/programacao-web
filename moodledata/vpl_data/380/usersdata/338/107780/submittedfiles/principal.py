"""
j_d_v1 = (" ", " ", " ")
j_d_v2 = (" ", " ", " ") 
j_d_v3 = (" ", " ", " ")     
"""       
cordenadas1 = ["00", "01", "02"]

cordenadas2 = ["10", "11", "12"] 

cordenadas3 = ["20", "21", "22"]         
from time import sleep
#def tabuleiro():
print(" ")
print(" ")
print(' ' + cordenadas1[0] + ' | ' + cordenadas1[1] + ' | ' + cordenadas1[2])
print(' ' + cordenadas2[0] + ' | ' + cordenadas2[1] + ' | ' + cordenadas2[2]) 
print(' ' + cordenadas3[0] + ' | ' + cordenadas3[1] + ' | ' + cordenadas3[2])        


nome_do_jogador = input("Digite o seu nome: ")
simb = input("Digite o simbolo com o qual vocÊ quer jogar [X ou O] : ")

while(True):
        if simb == "X" or simb == "O" :
            break
        else:
            simb = input("Digite um simbolo válido %s : " % nome_do_jogador)  
print("")
print("========================================================================")    
print("")
print("okay %s Seu simbolo foi aceito" % nome_do_jogador )
print("O seu simbolo será o: %s" % simb)
print("BOA SORTE!!!")
print("")
print("========================================================================") 

sleep(1)
print("")
print("agora sortearemos quem irá começar o jogo")
sleep(2)

import random
a = random.randint(1,2)
if a==1:
    print("Você começa %s" % nome_do_jogador ) 
   
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