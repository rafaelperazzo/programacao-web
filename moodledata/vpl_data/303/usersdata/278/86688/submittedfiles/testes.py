from minha_bib import *
print("Bem vindo ao JogoDaVelha do grupo ...")
nome = str(input("Qual o seu nome (ou apelido)? "))
simbolo_escolhido ()
sorteio ()
if sorteio=="humano":
    print("Vencedor do sorteio para início do jogo: "+nome+".")
if sorteio=="computador":
    print("Vencedor do sorteio para início do jogo: computador.")
