def solicitaNomeDoJogador():
    nome=str(input('Qual o seu nome ou (apelido)?'))
    return nome
    
# COLOQUE SEU PROGRAMA A PARTIR DAQUI
nomes=[["a","d"],["d","k"]]


print('Bem Vindo ao Jogo da Velha do Grupo "Deu Velha"')
nomes[0][0]=solicitaNomeDoJogador()
print(type(solicitaNomeDoJogador()))


