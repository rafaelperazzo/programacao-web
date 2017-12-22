nome_do_jogador = raw_input("Digite o seu nome: ")
simb = raw_input("Digite o simbolo com o qual vocÊ quer jogar [x ou o] : ")

while(True):
        if simb == "x" or simb == "o" :
            break
        else:
            simb = raw_input("Digite um simbolo válido %s : " % nome_do_jogador)  
print("")
print("========================================================================")    
print("")
print("okay %s Seu simbolo foi aceito" % nome_do_jogador )
print("O seu simbolo será o: %s" % simb)
print("BOA SORTE!!!")
    