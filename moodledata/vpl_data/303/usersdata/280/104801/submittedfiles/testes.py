from minha_bib import solicitaSimboloDoHumano
from minha_bib import sorteioPrimeiraJogada
name=[" ","PC"]
tab=[[" "," "," "], [" "," "," "], [" "," "," "]]


print("Bem vindo ao jogo da velha!" )
nome = str(input("Qual o seu nome (ou apelido)?: " ))
name[0]=nome
si=str(input("Qual símbolo você deseja utilizar no jogo? "))
simb=solicitaSimboloDoHumano(si)
jog_1=sorteioPrimeiraJogada(name)
print("Vencedor do sorteio para início do jogo: %s " %(jog_1))