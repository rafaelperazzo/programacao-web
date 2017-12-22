from minha_bib import solicitaSimboloDoHumano
from minha_bib import sorteioPrimeiraJogada
from minha_bib import jogadaComputador
from minha_bib import validaJogada
from minha_bib import jogadaHumana
from minha_bib import mostraTabuleiro
from minha_bib import verificaVencedor
from minha_bib import verificavelha

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
            print("Jogada do PC: ")
            tab=jogadaComputador(simb[1], tab)
            mostraTabuleiro(tab)
            win=verificaVencedor(tab,simb,name)
            print(win)
            if win != 0:
                break
            if win==0:
                velha=verificavelha(tab)
                if velha != 0:
                    break
                if velha==0:
                    cont = cont + 1
                    print("............")
                    print(cont)
        if order[0] == name[0]:
            play=int(input("Qual a sua jogada, %s? " %(name[0])))
            vplay=validaJogada(play, tab, name,)
            tab=jogadaHumana(vplay,simb,tab)
            mostraTabuleiro(tab)
            win=verificaVencedor(tab,simb,name)
            if win != 0:
                break
            if win==0:
                velha=verificavelha(tab)
                if velha != 0:
                    break
                if velha==0:
                    cont = cont + 1
                    print("............")
                    print(cont)
    if cont%2 != 0:
        if order[0] == "PC":
            play=int(input("Qual a sua jogada, %s? " %(name[0])))
            vplay=validaJogada(play, tab, name,)
            tab=jogadaHumana(vplay,simb,tab)
            mostraTabuleiro(tab)
            win=verificaVencedor(tab,simb,name)
            if win != 0:
                break
            if win==0:
                velha=verificavelha(tab)
                if velha != 0:
                    break
                if velha==0:
                    cont = cont + 1
                    print("............")
                    print(cont)
        if order[0] == name[0]:
            print("Jogada do PC: ")
            tab=jogadaComputador(simb[1], tab)
            mostraTabuleiro(tab)
            print(verificaVencedor(tab,simb,name))
            win=verificaVencedor(tab,simb,name)
            if win != 0:
                break
            if win==0:
                velha=verificavelha(tab)
                if velha != 0:
                    break
                if velha==0:
                    cont = cont + 1
                    print("............")
                    print(cont)