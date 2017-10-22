def solicitaNomeDoJogador():
    nome=str(input('Qual o seu nome ou (apelido)?'))
    return nome
def solicitaSimboloDoHumano():
    simbolo=input('Qual simbolo você deseja utilizar no jogo? ')
    while simbolo not in ('X', 'O'):
        simbolo=input('Qual simbolo você deseja utilizar no jogo? ')
    return simbolo()
# COLOQUE SEU PROGRAMA A PARTIR DAQUI
nomes=[["a","d"],["d","k"]]


print('Bem Vindo ao Jogo da Velha do Grupo "Deu Velha"')
nomes[0][0]=solicitaNomeDoJogador()
nomes[0][1]=solicitaSimboloDoHumano()
print(nomes)


