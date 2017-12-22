from minha_bib import solicitaSimboloDoHumano

simb=[" "," "]
tab=[[" "," "," "], [" "," "," "], [" "," "," "]]


print("Bem vindo ao jogo da velha!" )
nome = str("Qual o seu nome (ou apelido)?: " )
si=str(input("Qual símbolo você deseja utilizar no jogo? "))
solicitaSimboloDoHumano(si,simb)