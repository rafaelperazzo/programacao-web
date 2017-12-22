from minha_bib import solicitaSimboloDoHumano


tab=[[" "," "," "], [" "," "," "], [" "," "," "]]


print("Bem vindo ao jogo da velha!" )
nome = str("Qual o seu nome (ou apelido)?: " )
si=str(input("Qual símbolo você deseja utilizar no jogo? "))
solicitaSimboloDoHumano(si)
simb=solicitaSimboloDoHumano(si)
print(simb)