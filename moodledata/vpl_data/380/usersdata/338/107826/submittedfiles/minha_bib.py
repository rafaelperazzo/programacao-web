def nome_do_jogador():
    nome_do_jogador = input("Digite o seu nome: ")
    simb = input("Digite o simbolo com o qual vocÊ quer jogar [X ou O] : ")
    
def teste_de_simbolo():
while(True):
    if simb == "X" or simb == "O" :
        break
    else:
        simb = input("Digite um simbolo válido %s : " % nome_do_jogador)