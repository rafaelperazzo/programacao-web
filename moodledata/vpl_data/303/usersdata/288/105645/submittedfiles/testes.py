# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
#from minha_bib import *

velha="""  Jogadas      Posições jogáveis
   |   |           7 | 8 | 9
---+---+---       ---+---+---
   |   |           4 | 5 | 6
---+---+---       ---+---+---
   |   |           1 | 2 | 3
"""
# Listagem de posicoes (horizontal e vertical) para as posicoes do jogo.
# Numeração das posicoes ira facilitar o entendimento para jogabilidade.


posicoes = [
  None,  # Indice
  (5, 1), # 1
  (5, 5), # 2
  (5, 9), # 3
  (3, 1), # 4
  (3, 5), # 5
  (3, 9), # 6
  (1, 1), # 7
  (1, 5), # 8
  (1, 9), # 9
]

# Descrição das posicoes que ganham o jogo fazendo uma linha, um coluna, linha ou diagonal == win
# Os números representam as posicoes ganhadoras
win = [
      [ 1, 2, 3], #linha
      [ 4, 5, 6],
      [ 7, 8, 9],
      [ 7, 4, 1], #coluna
      [ 8, 5, 2],
      [ 9, 6, 3],
      [ 7, 5, 3], #diag
      [ 1, 5, 9]
    ]

# Tabuleiro é construido usndo string e gera lista

tabuleiro = []
for linha in velha.splitlines():
    tabuleiro.append(list(linha))

jogador = "X" # Começa jogando com X
jogando = True
jogada = 0 # Contador de jogadas
while True:
    for t in tabuleiro:  # Mostra o tabuleiro
        print("".join(t))
    if not jogando: # Termina após mostrar o último tabuleiro
        break
    if jogada == 9: # Se 9 jogadas, todas as posicoes já foram preenchidas
        print("Deu velha! Ninguém ganhou.")
        break
    jogada = int(input("Digite a posição a jogar 1-9 (jogador %s):" % jogador))
    if jogada<1 or jogada>9:
        print("Posição inválida")
        continue
# Verifica posição livre
if tabuleiro[posicoes[jogada][0]][posicoes[jogada][1]] != " ":
    print("Posição ja utilizada ocupada.")
    continue
# Marca a jogada p/ o jogador
tabuleiro[posicoes[jogada][0]][posicoes[jogada][1]] = jogador
# Verfica se ganhou
for p in win:
    for x in p:
        if tabuleiro[posicoes[x][0]][posicoes[x][1]] != jogador:
            break
    else: # Se o for terminar sem break, todas as posicoes de p pertencem ao mesmo jogador
        print("O jogador %s ganhou (%s): "%(jogador, p))
        jogando = False
        break
jogador = "X" if jogador == "O" else "O" # Alterna os jogador
jogada +=1 # Contador de jogadas







"""
m=int(input("Digite a quantidade n-s: "))
while m<2 or m>1000:
    m=int(input("Digite a quantidade n-s: "))
n=int(input("Digite a quantidade l-o: "))
while n<2 or n>1000:
    n=int(input("Digite a quantidade l-o: "))
matriz=[]
for i in range (0,m,1):
    linha=[]
    for j in range (0,n,1):
        a=(int(input("Digite o preço da quadra: ")))
        while a <1 or a >100:
            a=(int(input("Digite o preço da quadra: ")))
        linha.append (a)
    matriz.append(linha)
menor=100*m
for j in range (0,n,1):
    soma=0
    for i in range (0,m,1):
        soma+=matriz[i][j]
    if soma<menor:
        menor=soma
print (menor)





n=int(input('Digite um valor >=2: '))
while n<2:
    n=int(input('Digite um valor >=2: '))
a=[]
for i in range (0,n,1):
    b=[]
    for i in range (0,n,1):
        b.append(int(input('Digite os valores da matriz: ')))
    a.append(b)
print (a[i][i])
print (a[i][n-i])





lista1=[1,2,3,4]

print (lista1[len(lista1)+1])


n = 20
a = []
for i in range(0,n,1):
    a.append(input('Digite um valor: '))
print (a)

x=int(input('digite um valor 1: '))
y=int(input('digite um valor 2: '))
print (maximo(x,y))

if par(2):
    print ('sim')
else:
    print ('nao')



from minha_bib import *

a=int(input('digite a: '))
b=int(input('digite b: '))
print (f1(x,y))


a=-100
valor=avaliar(a)
print (valor)


if funcao(2,3,10):
    print ('S')
else:
    print ('n')



cronometro(20)


#print (fatorial(5))



#print(multiplicacao(2,3))


b=0
a=100
for i in range (0,a,1):
    if a%(i+1)!=0:
        b=b+1
print (b)

###########################
for i in range (0,10,1):
    print (i)

###########################

for i in rang (0,10,1): 
print (i)


while(True):
    while(True):
        n=int(input("Digite um numero inteiro positivo: "))
        if (n>=0):
            break
    f=1
    for i in range (2,n+1,1):
        f*=i
    print("%d!= %d" %(n,f))
    opt=input("Deseja continuar? [S ou N]")
    if (opt =="N"):
        print ("\n\nAte Breve")
        break

i=0
while i<10:
    print (i)
    
########################  

n=int(input("digite um numero n: "))
i=1
cont = 0
while i < n:
    if i%2==1:
        cont=cont+1
    i=i+1
print (cont)

##########################

for x in range (0,5,1):
    for y in range (0,5,1):
        print ("(%d,%d)" %(x,y))

##########################

n= int(input("Digite um numero: "))
i=2
contador=0
while (i<(n-1)):
    if n%i==0:
        comtador+=1
    i+=1
if contador>0:
    print ("%d Nao eh primo!" %n)
else:
    print ("%d Eh primo!" %n)

##########################


a= 30
b= 20
z=int(a/b)
print z

###########################

a=80
b=50
c=10
if a<b:
    print("comando 1")
else:
    if a<c:
        print ("comando 2")
    else b<c:
        print ("comando 3")
    print("pronto")

#########################

a=30
b=5
c=10
if a<b<c:
    print("comando 1")
else:
    if a<c<b:
        print("comando 2")
    else:
        print("comando 3")
    print("comando 4")
print("pronto")

###########################

a=3
b=5
c=10
if a<b:
    print ("comando 1")
else:
    if a<c:
        print("comando 2")
    else:
        if b<c:
            print ("comando 3")
print("pronto")

#########################



a=30
b=5
c=10
if a<b:
    print("comando 1")
else:
    if a<c:
        print("comando 2")
    else:
        if b<c:
            print("comando 3")
print ("pronto")
                
          
###########################    

a=int(input('Que horas são? [ 0-23 ]'))
if a < 0 or a > 23:
    print('Hora invalida')
elif a >= 3 and a <12:
    print('Bom dia')
elif a >= 12 and a< 18:
    print('Boa tarde')
else:
    print('boa noite')

############################

print("Seja bem vindo ao programa Quem é você!")
print("________________________________________")
nome= str(input("Me diga o seu nome: "))
print("\nOlá "+nome+". Farei algumas perguntas sobre você!")
idade=int(input("Me diga a sua idade: "))
print("\nok! Você tem %d anos." %idade)
altura=float(input("Me diga a sua altura em metros: "))
print("\nVocê tem %.2f metros de altura!" %altura)
print("\n\nIsso é tudo. Até a próxima, %s!" %nome)

###################################


a= float(input("digite o valor de a"))
a= a*10
print(a)


#####################################


float(input("digite um número em metros: "))
conversao=(unidade*100)
print("-----------------------------------")
print("o valor em centímetros é: %2.f" %conversao)


#################################


nota1 =float(input("digite sua nota (1): "))
nota2 =float(input("digite sua nota (2): "))
nota3 =float(input("digite sua nota (3): "))
nota4 =float(input("digite sua nota (4): "))
media=((nota1+nota2+nota3+nota4)/4)
print("sua média é: %2.f" %media)
"""










