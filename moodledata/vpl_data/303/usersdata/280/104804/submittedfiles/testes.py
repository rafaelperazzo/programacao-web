from minha_bib import solicitaSimboloDoHumano
from minha_bib import sorteioPrimeiraJogada
from minha_bib import jogadaComputador
from minha_bib import validaJogada
from minha_bib import jogadaHumana


name=[" ","PC"]
tab=[[" "," "," "], [" "," "," "], [" "," "," "]]


print("Bem vindo ao jogo da velha!" )
nome = str(input("Qual o seu nome (ou apelido)?: " ))
name[0]=nome
si=str(input("Qual símbolo você deseja utilizar no jogo? "))
simb=solicitaSimboloDoHumano(si)
jog_1=sorteioPrimeiraJogada(name)
jog_2=str(" ")
if jog_1==name[0]:
    jog_2=name[1]
if jog_1==name[1]:
    jog_2=name[0]
order=[jog_1, jog_2]
print (order)
print("Vencedor do sorteio para início do jogo: %s " %(jog_1))
cont=0


for i in range (0,9,1):
    if cont%2==0:
        if order[0] == "PC":
            jogadaComputador(simb[1])
            
        