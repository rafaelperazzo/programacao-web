from minha_bib import solicitaSimboloDoHumano

name=[" ","PC"]
tab=[[" "," "," "], [" "," "," "], [" "," "," "]]


print("Bem vindo ao jogo da velha!" )
nome = str(input("Qual o seu nome (ou apelido)?: " ))
name[0]=nome
print(name)
si=str(input("Qual símbolo você deseja utilizar no jogo? "))
simb=solicitaSimboloDoHumano(si)
print(simb)