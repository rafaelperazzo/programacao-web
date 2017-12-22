# -*- coding: utf-8 -*-
nome = str(input("Digite seu nome: "))
n = int(input("Digite a quantiddade de caracteres da sua senha: "))
senha = []
for i in range (0,n,1):
    senha.append(int(input("Digite um número para sua senha: ")))
for i in range (0,n-1,1):
    if senha[i] == senha[i+1]:
        print ("SENHA INVÁLIDA")
    else:
        print ("SENHA VÁLIDA")
    while senha[i] == senha[i+1]:
        for i in range (0,n,1):
            senha.append(int(input("Digite um número para sua senha: ")))
          





n = int(input("Digite a quantidade de elementos da lista: "))
lista = []
for i in range (0,n,1):
    lista.append(int(input("Digite um número para a lista: ")))
cont = 0
lista_pares = []
for i in range (0,n,1):
    if lista[i]%2==0:
        lista_pares.append(lista[i])
m = len(lista_pares)
cont = 0
for i in range (0,m-1,1):
    if lista_pares[i] == lista_pares[i+1]:
        cont += 1
        
lista_impares = []
for i in range (0,n,1):
    if lista[i]%2!=0:
        lista_impares.append(lista[i])
print(lista_impares)
        



















from minha_bib import *

# COLOQUE SEU PROGRAMA A PARTIR DAQUI
import random 

print("Bem vindo ao Jogo Da Velha do grupo 'F'")
print ("_________________________________________")
nome = str(input("\nQual o seu nome? "))
while True:
    tab = [' '] * 10
    simboloVoce, simboloComputador = solicitaSimboloDoHumano()
    turn = sorteioPrimeiraJogada()
    print ("\n")
    print ("\nPosições jogáveis")
    print ("\n 0 0 | 0 1 | 0 2 ")
    print ("-----+-----+----")
    print (" 1 0 | 1 1 | 1 2 ")
    print ("-----+-----+----") 
    print (" 2 0 | 2 1 | 2 2 ")
    print ("\n")  
    print ("______________________________________________")
    print ("\n Começou!")
    if turn=="Voce":
        print("\nVencedor do sorteio para início do jogo: "+nome+" ")
    else:
        print("\nVencedor do sorteio para início do jogo: computador ")
    print ("\n")
    i = 0

    while i<1:
        if turn == "Voce":
            desenhaTabuleiro(tab)
            movimento = jogadaHumana(tab)
            jogada(tab, simboloVoce, movimento)

            if verificaVencedor(tab, simboloVoce):
                desenhaTabuleiro(tab)
                print("Vencedor: "+nome+"")
                i=i+1
            else:
                if completo(tab):
                    desenhaTabuleiro(tab)
                    print("Deu Velha!")
                    break
                else:
                    turn = "Computador"

        else:
            movimento = jogadaComputador(tab, simboloComputador)
            jogada(tab, simboloComputador, movimento)

            if verificaVencedor(tab, simboloComputador):
                desenhaTabuleiro(tab)
                print("Vencedor: Computador")
                i=i+1
            else:
                if completo(tab):
                    desenhaTabuleiro(tab)
                    print("Deu Velha!")
                    break
                else:
                    turn = "Voce"

    if jogarNovamente():
        continue
    else:
        break
print ("\nObrigado por jogar, "+nome+". Até mais!")
